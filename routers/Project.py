# 接口层  curd调用models 接口调用 schemas 和 curd  schemas接口请求方法（）内， curd在请求体内 也就是 ：下面
from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from model import schemas, curd
from model.curd import get_db

project = APIRouter()


@project.get("/projects/", response_model=List[schemas.Project])
def read_all_projects(db: Session = Depends(get_db)):
    """
    获取所有项目的接口。

    Args:
        db (Session): 数据库会话对象。

    Returns:
        List[schemas.Project]: 包含所有项目信息的列表。
    """
    return curd.get_all_projects(db=db)


@project.get("/projects/{project_id}", response_model=schemas.Project)
def read_project_with_test_cases(project_id: int, db: Session = Depends(get_db)):
    """
    获取包含测试用例的项目的接口。

    Args:
        project_id (int): 要查询的项目 ID。
        db (Session): 数据库会话对象。

    Returns:
        schemas.Project: 包含关联测试用例的项目信息。
    """
    return curd.get_project_with_test_cases(db=db, project_id=project_id)


@project.post("/projects/", response_model=schemas.Project)
def create_project(new_project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    """
    创建项目接口。

    Args:
        new_project (schemas.ProjectCreate): 项目的创建信息。
        db (Session): 数据库会话对象。

    Returns:
        schemas.Project: 新创建的项目信息。
    """
    return curd.create_project(db=db, project=new_project)


@project.put("/projects/{project_id}", response_model=schemas.Project)
def update_project(project_id: int, renewal_project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    """
    更新项目接口。

    Args:
        project_id (int): 要更新的项目 ID。
        renewal_project (schemas.ProjectCreate): 更新后的项目信息。
        db (Session): 数据库会话对象。

    Returns:
        schemas.Project: 更新后的项目信息。
    """
    return curd.update_project(db=db, project_id=project_id, project=renewal_project)


@project.delete("/projects/{project_id}", response_model=schemas.Project)
def delete_project(project_id: int, db: Session = Depends(get_db)):
    """
    删除项目接口。

    Args:
        project_id (int): 要删除的项目 ID。
        db (Session): 数据库会话对象。

    Returns:
        schemas.Project: 删除的项目信息。
    """
    return curd.delete_project(db=db, project_id=project_id)
