from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import json,uvicorn,time
from function.getData import get_data
from pydantic import BaseModel

app = FastAPI(
    debug=False,
    docs_url=None,
)

# 设置静态文件目录
app.mount("/static", StaticFiles(directory="static"), name="static")

# 设置模板目录
templates = Jinja2Templates(directory="templates")

@app.get("/testdelay")
async def testdelay(request: Request):
    return None

@app.get("/", response_class=HTMLResponse)
async def read_index(request: Request):
    # 从data.json中读取json数据
    with open("data/days.json", "r",encoding='utf-8') as f:
        data = f.read()
    days = json.loads(data)
    timestamp = int(time.time())
    return templates.TemplateResponse("index.html", {"request": request, "days": days, "timestamp": timestamp})

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8133,reload=False,)
