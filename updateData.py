import asyncio,time
from function.getData import get_data

if __name__ == "__main__":
    while True:
        # 打印开始时间2021-05-04 00:00:00
        print("开始时间" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        asyncio.run(get_data())
        # 打印结束时间2021-05-04 00:00:00
        print("结束时间" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # 休眠10分钟,这里需要使用协程的方式进行休眠
        asyncio.run(asyncio.sleep(600))