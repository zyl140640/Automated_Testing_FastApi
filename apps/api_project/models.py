# models.py - 数据库模型，用于被调用方

from sqlalchemy import Column, Integer, String, DateTime, func
from sqlalchemy.orm import relationship

from tools.database import Base  # 导入数据库基类，可能在其他文件中定义


class Project(Base):
    __tablename__ = 'projects'  # 表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False, comment="项目ID")
    name = Column(String(255), nullable=False, comment="项目名称")
    project_path = Column(String(255), nullable=False, comment="存放地址")
    creator = Column(String(255), nullable=False, comment="项目创建人")
    creation_time = Column(DateTime, server_default=func.now(), comment="项目创建时间")
    test_cases = relationship("TestCase", backref='project')  # 定义与TestCase的关系，backref表示反向引用
