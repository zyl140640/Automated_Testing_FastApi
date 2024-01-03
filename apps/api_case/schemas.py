# schemas.py - 数据校验，用于请求
from datetime import datetime

from pydantic import BaseModel


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

# class TestCaseTestStep(TestCaseBase):
#     id: int
#     creation_time: datetime
#     test_steps: List[TestStep]
