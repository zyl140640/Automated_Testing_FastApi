# curd.py  用于编写sql语句 在接口处调用函数方法即可  curd调用models
from sqlalchemy.orm import Session, selectinload

from apps.api_project import schemas, models


# 所有与数据库相关的增删改查的操作方法
# 创建操作
def create_project(db: Session, project: schemas.ProjectCreate):
    """
    创建项目的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        project (schemas.ProjectCreate): 从请求接收的项目数据。

    Returns:
        models.Project: 创建的项目对象。
    """
    db_project = models.Project(**project.model_dump())
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project


# 更新操作
def update_project(db: Session, project_id: int, project: schemas.ProjectCreate):
    """
    更新项目的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        project_id (int): 要更新的项目 ID。
        project (schemas.ProjectCreate): 更新的项目数据。

    Returns:
        models.Project: 更新后的项目对象。
    """
    db_project = db.query(models.Project).filter_by(id=project_id).first()
    if db_project:
        for key, value in project.model_dump().items():
            setattr(db_project, key, value)
        db.commit()
        db.refresh(db_project)
    return db_project


# 删除操作
def delete_project(db: Session, project_id: int):
    """
    删除项目的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        project_id (int): 要删除的项目 ID。
    """
    db.query(models.Project).filter_by(id=project_id).delete()
    db.commit()


# 查询
# 获取所有项目
def get_all_projects(db: Session):
    """
    获取所有项目的数据库操作。

    Args:
        db (Session): 数据库会话对象。

    Returns:
        List[models.Project]: 包含所有项目对象的列表。
    """
    return db.query(models.Project).all()


# 多表联查
def get_project_with_test_cases(db: Session, project_id: int):
    """
    获取包含测试用例的项目的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        project_id (int): 要查询的项目 ID。

    Returns:
        models.Project: 包含关联测试用例的项目对象。
    """
    return db.query(models.Project).filter_by(id=project_id).options(
        selectinload(models.Project.test_cases)
    ).first()
