# schemas.py - 数据校验，用于请求
from datetime import datetime
from typing import List

from pydantic import BaseModel


# 项目基础信息
class ProjectBase(BaseModel):
    name: str  # 项目名称
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


# 测试用例基础信息
class TestCaseBase(BaseModel):
    name: str  # 测试用例名称
    creator: str  # 测试用例创建人
    test_report: str  # 测试报告


# 用于在创建测试用例时接收数据
class TestCaseCreate(TestCaseBase):
    pass


# 用于返回测试用例信息
class TestCase(TestCaseBase):
    id: int  # 测试用例ID
    project_id: int  # 项目ID
    creation_time: datetime  # 测试用例创建时间
    test_report: str  # 测试报告存放地址

    class Config:
        from_attributes = True  # 启用ORM模式，以便支持SQLAlchemy模型


# 测试步骤基础信息
class TestStepBase(BaseModel):
    name: str  # 测试步骤名称
    element_mode: int  # 元素定位方式
    element_path: str  # 元素定位路径
    element_data: str  # 元素测试数据
    creator: str  # 测试用例创建人


# 用于在创建测试步骤时接收数据
class TestStepCreate(TestStepBase):
    pass


# 用于返回测试步骤信息
class TestStep(TestStepBase):
    id: int  # 测试步骤ID
    test_case_id: int  # 测试用例ID
    creation_time: datetime  # 测试步骤创建时间

    class Config:
        from_attributes = True  # 启用ORM模式，以便支持SQLAlchemy模型


# 返回项目下的测试数据
class ProjectTestCase(ProjectBase):
    id: int
    creation_time: datetime
    test_cases: List[TestCase]


class TestCaseTestStep(TestCaseBase):
    id: int
    creation_time: datetime
    test_steps: List[TestStep]
