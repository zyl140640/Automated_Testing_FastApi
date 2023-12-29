import logging.config
import os

import uvicorn
from fastapi import FastAPI, Request, Response
from starlette.middleware.cors import CORSMiddleware

from model import models
from model.database import engine, SessionLocal
from routers.Project import project
from routers.TestCase import testcase
from routers.TestStep import teststep

# 配置日志
models.Base.metadata.create_all(bind=engine)
logging.config.fileConfig(fname=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini'),
                          disable_existing_loggers=False)

app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


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
