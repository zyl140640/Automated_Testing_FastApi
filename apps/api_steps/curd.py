# curd.py  用于编写sql语句 在接口处调用函数方法即可  curd调用models
from sqlalchemy.orm import Session

from apps.api_steps import schemas, models


# 所有与数据库相关的增删改查的操作方法
# 创建操作


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
