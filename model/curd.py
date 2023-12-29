# curd.py  用于编写sql语句 在接口处调用函数方法即可  curd调用models
from sqlalchemy.orm import Session

from apps.dependencies import current_time
from model import models, schemas
from model.database import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 所有与数据库相关的增删改查的操作方法
# 根据项目ID查询获取项目信息
def get_project(db: Session, project_id):
    return db.query(models.Project).get(project_id)


# 根据查询获取所有项目信息
def get_project_all(db: Session):
    return db.query(models.Project).all()


# 创建项目
def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(
        project_name=project.project_name,
        Project_creator=project.Project_creator,
        Project_creation_time=current_time()  # 确保current_time()函数存在并返回正确的时间
    )
    db.add(db_project)
    db.commit()
    db.refresh(db_project)  # 可选步骤：如果需要在后续操作中使用到刚刚添加的项目的其他属性，可以保留这行代码
    return db_project
