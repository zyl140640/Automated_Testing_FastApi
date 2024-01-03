# models.py - 数据库模型，用于被调用方

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from tools.database import Base  # 导入数据库基类，可能在其他文件中定义


class TestCase(Base):
    __tablename__ = 'test_cases'  # 表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, comment="测试用例ID")
    project_id = Column(Integer, ForeignKey('projects.id'), comment="项目ID")  # 外键关联到projects表的id字段
    name = Column(String(255), nullable=False, comment="测试用例名称")
    test_report = Column(String(255), nullable=True, comment="测试报告存放地址")
    creator = Column(String(255), nullable=False, comment="测试用例创建人")
    creation_time = Column(DateTime, server_default=func.now(), comment="测试用例创建时间")
    test_steps = relationship("TestStep", backref='test_case')  # 定义与TestStep的关系，backref表示反向引用
