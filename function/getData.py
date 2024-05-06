import asyncio,httpx,json,traceback
from config import settings
from datetime import datetime, timedelta

def get_days_key_name(date_string):
    # 定义日期格式
    date_format = "%Y-%m-%d %H:%M:%S"

    # 将字符串转换为datetime对象
    date_obj = datetime.strptime(date_string, date_format)

    # 获取星期几（返回的是一个数字，其中0代表周一，6代表周日）
    weekday_number = date_obj.weekday()

    # 将数字转换为星期几的名称
    weekdays = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"]
    weekday_name = weekdays[weekday_number]

    # 格式化日期为“月份日”，确保兼容所有平台
    formatted_date = date_obj.strftime("%m月%d日").lstrip('0').replace('月0', '月')

    # 合并新的日期格式和星期名称
    result = f"{formatted_date} {weekday_name}"

    return result

async def get_data_likedong(url,platform):
    # 用httpx进行异步请求
    ret_data = []
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            return {
                "status": False,
                "message": "请求失败"
            }
        data = json.loads(response.text)
        # 对data进行处理
        content = data.get('response', [])[0].get("content", [])
        if len(content) == 0:
            return {
                "status": False,
                "message": "数据为空"
            }
        for item in content:
            temp = {}
            # 获取标题
            temp['title'] = item.get("title", "")
            # 获取活动开始时间
            temp['start_time'] = item.get("start_time", "")
            # 获取活动结束时间
            temp['end_time'] = item.get("end_time", "")
            # 同时根据活动时间获取days中符合格式的keyname, 例如"5月4日 周六"
            temp['days_key_name'] = get_days_key_name(temp['start_time'])
            # 生成活动时间段
            temp['time_range'] = (temp['start_time'].split(" ")[1] + "-" + temp['end_time'].split(" ")[1]).replace("00:00","00")
            # 获取活动地点
            temp['venue_name'] = item.get("venue_name", "")
            # 最多参与人数
            temp['max_participants'] = item.get("participants_num", "")
            # 当前参与人数
            temp['current_participants'] = item.get("applied_num", "")
            # 组织者
            temp['organizer'] = item.get("contact_name", "")
            # 当前平台
            temp['platformIconUrl'] = "static/icon/likedong.png"
            # 跳转链接
            temp['jumpLink'] = platform['JumpLink']

            ret_data.append(temp)
    return {
        "status": True,
        "data": ret_data
    }
        
        
async def get_data_shandong(url,club,platform):
    # 用httpx进行异步请求
    ret_data = []
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code != 200:
            print("请求失败: ", response.status_code)
            return {
                "status": False,
                "message": "请求失败"
            }
        data = json.loads(response.text)
        # 对data进行处理
        records = data.get("result", {}).get("records", [])
        if len(records) == 0:
            print("数据为空")
            return {
                "status": False,
                "message": "数据为空"
            }
        for item in records:
            temp = {}
            # 获取标题
            temp['title'] = club['ClubName'] + "|" + item.get("activityTitle", "")
            # 获取活动开始时间
            activityDate = item.get("activityDate", "")
            startTime = item.get("startTime", "")
            endTime = item.get("endTime", "")
            temp['start_time'] = activityDate + " " + startTime + ":00"
            # 获取活动结束时间
            temp['end_time'] = activityDate + " " + endTime + ":00"
            # 同时根据活动时间获取days中符合格式的keyname, 例如"5月4日 周六"
            temp['days_key_name'] = get_days_key_name(temp['start_time'])
            # 生成活动时间段
            temp['time_range'] = (temp['start_time'].split(" ")[1] + "-" + temp['end_time'].split(" ")[1]).replace("00:00","00")
            # 获取活动地点
            temp['venue_name'] = item.get("activityAddress", "")
            # 最多参与人数
            temp['max_participants'] = item.get("needMemberNum", "")
            # 当前参与人数
            temp['current_participants'] = item.get("applyMemberNum", "")
            # 组织者
            temp['organizer'] = item.get("organizerName", "")
            # 当前平台
            temp['platformIconUrl'] = "static/icon/shandong.png"
            # 跳转链接
            temp['jumpLink'] = platform['JumpLink']

            ret_data.append(temp)
    return {
        "status": True,
        "data": ret_data
    
    }



async def get_data():
    days = {}
    # days 进行初始化,插入当前日期往后的n天,并且以"5月4日 周六"为key
    for i in range(settings.view_days):
        date = datetime.now().date() + timedelta(days=i)
        key_name = get_days_key_name(date.strftime("%Y-%m-%d %H:%M:%S"))
        days[key_name] = []
    for club in settings.ClubInfo:
        for platform in club["ClubPlatform"]:
            url = settings.UrlInfo[platform["PlatformName"]].format(platform["ClubID"])
            print(f"开始检索{club['ClubName']},平台{platform['PlatformName']}")
            print(f"请求地址: {url}")
            try:
                # 对当前平台进行异步请求
                if platform["PlatformName"] == "likedong":
                    data = await get_data_likedong(url,platform)
                elif platform["PlatformName"] == "shandong":
                    data = await get_data_shandong(url,club,platform)
            except:
                print(f"请求失败,{traceback.format_exc()}")
                # 构造一个失败的data
                data = {
                    "status": False,
                    "message": "请求失败"
                }
                continue
            if not data["status"]:
                print("获取数据失败: ", data)
                continue
            # 对data进行筛选,将符合days中"5月4日 周六"的数据插入到days中
            for item in data['data']:
                if item["days_key_name"] in days:
                    days[item["days_key_name"]].append(item)
    
    # print("days: ", days)
    # 将days写入json文件
    with open("data/days.json", "w",encoding='utf-8') as f:
        f.write(json.dumps(days, ensure_ascii=False))

    return True



