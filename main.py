import os

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import logging.config
from model import models
from model.database import engine
from routers.Project import project
from routers.TestCase import testcase
from routers.TestStep import teststep

# 配置日志
models.Base.metadata.create_all(bind=engine)
logging.config.fileConfig(fname=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini'),
                          disable_existing_loggers=False)

app = FastAPI()

# 解决跨域问题允许所有人访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 路由
app.include_router(project, prefix="/project", tags=["项目管理中心"])
app.include_router(testcase, prefix="/testcase", tags=["用例管理中心"])
app.include_router(teststep, prefix="/test_steps", tags=["步骤管理中心"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
