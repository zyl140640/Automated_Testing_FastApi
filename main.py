import logging.config
import os

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from apps.api_case.TestCase import testcase
from apps.api_project import models as project_models
from apps.api_case import models as case_models
from apps.api_project.Project import project
from apps.api_steps import models as steps_models
from apps.api_steps.TestStep import teststep

from tools.database import engine

# 定义模型列表
models_list = [project_models, case_models, steps_models]
# 使用循环创建所有表格
for models_module in models_list:
    models_module.Base.metadata.create_all(bind=engine)
# 配置日志
logging.config.fileConfig(fname=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'logging.ini'),
                          disable_existing_loggers=False)

app = FastAPI(title="Automated_Testing_FastApi", summary="Automated Testing的后端API接口", version="1.0")

# session 中间件
# # @app.middleware("http")
# # async def db_session_middleware(request: Request, call_next):
# #     response = None  # 初始化 response 变量
# #     try:
# #         request.state.db = SessionLocal()
# #         response = await call_next(request)
# #     finally:
# #         request.state.db.close()
# #         return response  # 将 response 返回至上层


# 解决跨域问题允许所有人访问
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# API路由
app.include_router(project, prefix="/projects", tags=["项目管理中心"])
app.include_router(testcase, prefix="/testcases", tags=["用例管理中心"])
app.include_router(teststep, prefix="/test_steps", tags=["步骤管理中心"])


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
