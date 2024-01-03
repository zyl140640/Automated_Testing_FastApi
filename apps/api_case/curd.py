# curd.py  用于编写sql语句 在接口处调用函数方法即可  curd调用models
from sqlalchemy.orm import Session, selectinload

from apps.api_case import schemas, models


# 所有与数据库相关的增删改查的操作方法
# 创建操作


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

    # 更新操作


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


# 删除操作


def delete_test_case(db: Session, test_case_id: int):
    """
    删除测试用例的数据库操作。

    Args:
        db (Session): 数据库会话对象。
        test_case_id (int): 要删除的测试用例 ID。
    """
    db.query(models.TestCase).filter_by(id=test_case_id).delete()
    db.commit()


# 查询


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
