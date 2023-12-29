# models.py  数据库模型 用于被调用方

from sqlalchemy import Column, String, Integer

from model.database import Base, engine


class Project(Base):
    __tablename__ = 'project'  # 数据库表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=True, comment="项目ID")
    project_name = Column(String(255), nullable=False, comment="项目名称")
    Project_creator = Column(String(255), nullable=False, comment="项目创建人")
    Project_creation_time = Column(String(255), nullable=False, comment="项目创建时间")
    # testcases = relationship("testcase", backref='projects')


class TestCase(Base):
    __tablename__ = 'test_case'  # 数据库表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=True, comment="测试用例ID")
    test_case_name = Column(String(255), nullable=False, comment="测试用例名称")
    project_id = Column(Integer, comment="项目ID")
    test_case_creator = Column(String(255), nullable=False, comment="测试用例创建人")
    test_case_creation_time = Column(String(255), nullable=False, comment="测试用例创建时间")
    test_report = Column(String(255), nullable=True, comment="测试报告存放地址")


class TestStep(Base):
    __tablename__ = 'test_step'  # 数据库表名
    id = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=True, comment="测试步骤ID")
    test_step_name = Column(String(255), nullable=False, comment="测试步骤名称")
    test_case_id = Column(Integer, comment="测试用例ID")
    element_mode = Column(Integer, nullable=False, comment="元素定位方式")
    element_path = Column(String(255), nullable=False, comment="元素定位路径")
    element_data = Column(String(255), nullable=False, comment="元素测试数据")
    test_step_creator = Column(String(255), nullable=False, comment="测试用例创建人")
    test_step_creation_time = Column(String(255), nullable=False, comment="测试用例创建时间")
    test_report = Column(String(255), nullable=True, comment="测试报告存放地址")


if __name__ == '__main__':
    Base.metadata.create_all(engine)
