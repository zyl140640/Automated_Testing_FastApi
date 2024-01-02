# curd.py  用于编写sql语句 在接口处调用函数方法即可  curd调用models
from sqlalchemy.orm import Session, selectinload

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


def create_test_case(db: Session, test_case: schemas.TestCaseCreate, project_id: int):
    """
    创建测试用例的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_case (schemas.TestCaseCreate): 从请求接收的测试用例数据。
        project_id (int): 关联的项目 ID。

    Returns:
        models.TestCase: 创建的测试用例对象。
    """
    db_test_case = models.TestCase(**test_case.model_dump(), project_id=project_id)
    db.add(db_test_case)
    db.commit()
    db.refresh(db_test_case)
    return db_test_case


def create_test_step(db: Session, test_step: schemas.TestStepCreate, test_case_id: int):
    """
    创建测试步骤的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_step (schemas.TestStepCreate): 从请求接收的测试步骤数据。
        test_case_id (int): 关联的测试用例 ID。

    Returns:
        models.TestStep: 创建的测试步骤对象。
    """
    db_test_step = models.TestStep(**test_step.model_dump(), test_case_id=test_case_id)
    db.add(db_test_step)
    db.commit()
    db.refresh(db_test_step)
    return db_test_step


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


def update_test_case(db: Session, test_case_id: int, test_case: schemas.TestCaseCreate):
    """
    更新测试用例的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_case_id (int): 要更新的测试用例 ID。
        test_case (schemas.TestCaseCreate): 更新的测试用例数据。

    Returns:
        models.TestCase: 更新后的测试用例对象。
    """
    db_test_case = db.query(models.TestCase).filter_by(id=test_case_id).first()
    if db_test_case:
        for key, value in test_case.model_dump().items():
            setattr(db_test_case, key, value)
        db.commit()
        db.refresh(db_test_case)
    return db_test_case


def update_test_step(db: Session, test_step_id: int, test_step: schemas.TestStepCreate):
    """
    更新测试步骤的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_step_id (int): 要更新的测试步骤 ID。
        test_step (schemas.TestStepCreate): 更新的测试步骤数据。

    Returns:
        models.TestStep: 更新后的测试步骤对象。
    """
    db_test_step = db.query(models.TestStep).filter_by(id=test_step_id).first()
    if db_test_step:
        for key, value in test_step.model_dump().items():
            setattr(db_test_step, key, value)
        db.commit()
        db.refresh(db_test_step)
    return db_test_step


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


def delete_test_case(db: Session, test_case_id: int):
    """
    删除测试用例的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_case_id (int): 要删除的测试用例 ID。
    """
    db.query(models.TestCase).filter_by(id=test_case_id).delete()
    db.commit()


def delete_test_step(db: Session, test_step_id: int):
    """
    删除测试步骤的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_step_id (int): 要删除的测试步骤 ID。
    """
    db.query(models.TestStep).filter_by(id=test_step_id).delete()
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


# 获取所有测试用例
def get_all_test_cases(db: Session):
    """
    获取所有测试用例的数据库操作。

    Args:
        db (Session): 数据库会话对象。

    Returns:
        List[models.TestCase]: 包含所有测试用例对象的列表。
    """
    return db.query(models.TestCase).all()


# 获取所有测试步骤
def get_all_test_steps(db: Session):
    """
    获取所有测试步骤的数据库操作。

    Args:
        db (Session): 数据库会话对象。

    Returns:
        List[models.TestStep]: 包含所有测试步骤对象的列表。
    """
    return db.query(models.TestStep).all()


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


def get_test_case_with_steps(db: Session, test_case_id: int):
    """
    获取包含测试步骤的测试用例的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_case_id (int): 要查询的测试用例 ID.

    Returns:
        models.TestCase: 包含关联测试步骤的测试用例对象。
    """
    return db.query(models.TestCase).filter_by(id=test_case_id).options(
        selectinload(models.TestCase.test_steps)
    ).first()
