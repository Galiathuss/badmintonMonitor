import asyncio,time
from function.getData import get_data
from config import settings
from rich.progress import Progress


def precise_countdown(duration_seconds):
    with Progress() as progress:
        task = progress.add_task("倒计时", total=duration_seconds)
        start_time = time.time()  # 获取当前时间
        while not progress.finished:
            elapsed = time.time() - start_time  # 计算已过时间
            progress.update(task, completed=int(elapsed))
            time.sleep(0.1)  # 每0.1秒更新一次
            if elapsed >= duration_seconds:
                break


if __name__ == "__main__":
    while True:
        # 打印开始时间2021-05-04 00:00:00
        print("开始时间" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        asyncio.run(get_data())
        # 打印结束时间2021-05-04 00:00:00
        print("结束时间" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        # 休眠30分钟
        precise_countdown(settings.sleep_time)