import aiohttp
import asyncio
import time

async def send_post_request():
    # 定义你的 FastAPI 服务的 URL
    # url = "http://104.219.236.45:8133/testdelay"
    url = "http://127.0.0.1:8133/testdelay"

    # 创建要发送的数据
    data = {"ts": time.time() * 1000}

    # 创建一个 aiohttp session
    async with aiohttp.ClientSession() as session:
        # 发送 POST 请求
        async with session.post(url, json=data) as response:
            # 等待响应并打印结果
            print("Status Code:", response.status)
            response_data = await response.json()
            print("Response Body:", response_data)

# 运行异步函数
asyncio.run(send_post_request())
