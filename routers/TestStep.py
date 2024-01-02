from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model import schemas, curd
from model.curd import get_db

teststep = APIRouter()


# 获取所有测试步骤的接口
@teststep.get("/test_steps/", response_model=List[schemas.TestStep])
def read_all_test_steps(db: Session = Depends(get_db)):
    """
    获取所有测试步骤的接口。

    Args:
        db (Session): 数据库会话对象。

    Returns:
        List[schemas.TestStep]: 包含所有测试步骤信息的列表。
    """
    return curd.get_all_test_steps(db=db)


# 创建测试步骤接口
@teststep.post("/test_steps/", response_model=schemas.TestStep)
def create_test_step(test_step: schemas.TestStepCreate, test_case_id: int, db: Session = Depends(get_db)):
    return curd.create_test_step(db=db, test_step=test_step, test_case_id=test_case_id)


# 更新测试步骤接口
@teststep.put("/test_steps/{test_step_id}", response_model=schemas.TestStep)
def update_test_step(test_step_id: int, test_step: schemas.TestStepCreate, db: Session = Depends(get_db)):
    return curd.update_test_step(db=db, test_step_id=test_step_id, test_step=test_step)


# 删除测试步骤接口
@teststep.delete("/test_steps/{test_step_id}", response_model=schemas.TestStep)
def delete_test_step(test_step_id: int, db: Session = Depends(get_db)):
    return curd.delete_test_step(db=db, test_step_id=test_step_id)
