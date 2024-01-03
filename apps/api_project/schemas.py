# schemas.py - 数据校验，用于请求
from datetime import datetime
from typing import List

from pydantic import BaseModel


# 项目基础信息
class ProjectBase(BaseModel):
    name: str  # 项目名称
    project_path: str  # 项目存放地址
    creator: str  # 项目创建人


# 用于在创建项目时接收数据
class ProjectCreate(ProjectBase):
    pass


# 用于返回项目信息
class Project(ProjectBase):
    id: int  # 项目ID
    creation_time: datetime  # 项目创建时间

    class Config:
        from_attributes = True  # 启用ORM模式，以便支持SQLAlchemy模型

# # 返回项目下的测试数据
# class ProjectTestCase(ProjectBase):
#     id: int
#     creation_time: datetime
#     test_cases: List[TestCase]
