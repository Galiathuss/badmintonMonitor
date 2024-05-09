import aiohttp
import asyncio
import time

async def send_post_request():
    # 定义你的 FastAPI 服务的 URL
    url = "http://badminton.mcdlmail.com/testdelay"
    # url = "http://127.0.0.1:8133/testdelay"

    ts = time.time() * 1000
    # 创建一个 aiohttp session
    async with aiohttp.ClientSession() as session:
        # 发送 POST 请求
        async with session.get(url) as response:
            # 打印响应状态码
            print("Response Status:", response.status)
            print(time.time() * 1000- ts)

# 运行异步函数
asyncio.run(send_post_request())
