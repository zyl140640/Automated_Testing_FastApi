from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from apps.api_case import schemas, curd
from depends.session import get_db

testcase = APIRouter()


@testcase.get("/test_cases/", response_model=List[schemas.TestCase])
def read_all_test_cases(db: Session = Depends(get_db)):
    """
    获取所有测试用例的接口。

    Args:
        db (Session): 数据库会话对象。

    Returns:
        List[schemas.TestCase]: 包含所有测试用例信息的列表。
    """
    return curd.get_all_test_cases(db=db)


# 创建测试用例接口
@testcase.post("/test_cases/", response_model=schemas.TestCase)
def create_test_case(test_case: schemas.TestCaseCreate, project_id: int, db: Session = Depends(get_db)):
    return curd.create_test_case(db=db, test_case=test_case, project_id=project_id)


# 获取测试用例接口
@testcase.get("/test_cases/{test_case_id}", response_model=schemas.TestCase)
def read_test_case(test_case_id: int, db: Session = Depends(get_db)):
    return curd.get_test_case_with_steps(db=db, test_case_id=test_case_id)


# 更新测试用例接口
@testcase.put("/test_cases/{test_case_id}", response_model=schemas.TestCase)
def update_test_case(test_case_id: int, test_case: schemas.TestCaseCreate, db: Session = Depends(get_db)):
    return curd.update_test_case(db=db, test_case_id=test_case_id, test_case=test_case)


# 删除测试用例接口
@testcase.delete("/test_cases/{test_case_id}")
def delete_test_case(test_case_id: int, db: Session = Depends(get_db)):
    curd.delete_test_case(db=db, test_case_id=test_case_id)
    return {
        "status": "success",
        "message": "Deleted successfully",
    }
