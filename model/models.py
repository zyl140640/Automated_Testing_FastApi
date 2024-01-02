# models.py - 数据库模型，用于被调用方

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship

from model.database import Base  # 导入数据库基类，可能在其他文件中定义


class Project(Base):
    __tablename__ = 'projects'  # 表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, comment="项目ID")
    name = Column(String(255), nullable=False, comment="项目名称")
    creator = Column(String(255), nullable=False, comment="项目创建人")
    creation_time = Column(DateTime, server_default=func.now(), comment="项目创建时间")
    test_cases = relationship("TestCase", backref='project')  # 定义与TestCase的关系，backref表示反向引用


class TestCase(Base):
    __tablename__ = 'test_cases'  # 表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, comment="测试用例ID")
    name = Column(String(255), nullable=False, comment="测试用例名称")
    project_id = Column(Integer, ForeignKey('projects.id'), comment="项目ID")  # 外键关联到projects表的id字段
    creator = Column(String(255), nullable=False, comment="测试用例创建人")
    creation_time = Column(DateTime, server_default=func.now(), comment="测试用例创建时间")
    test_report = Column(String(255), nullable=True, comment="测试报告存放地址")
    test_steps = relationship("TestStep", backref='test_case')  # 定义与TestStep的关系，backref表示反向引用


class TestStep(Base):
    __tablename__ = 'test_steps'  # 表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, comment="测试步骤ID")
    name = Column(String(255), nullable=False, comment="测试步骤名称")
    test_case_id = Column(Integer, ForeignKey('test_cases.id'), comment="测试用例ID")  # 外键关联到test_cases表的id字段
    element_mode = Column(Integer, nullable=False, comment="元素定位方式")
    element_path = Column(String(255), nullable=False, comment="元素定位路径")
    element_data = Column(String(255), nullable=True, comment="元素测试数据")
    creator = Column(String(255), nullable=False, comment="测试用例创建人")
    creation_time = Column(DateTime, server_default=func.now(), comment="测试用例创建时间")
