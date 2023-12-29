# 接口层  curd调用models 接口调用 schemas 和 curd  schemas接口请求方法（）内， curd在请求体内 也就是 ：下面
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model import schemas
from model.curd import get_project, get_db, create_project, get_project_all

project = APIRouter()


@project.get("/list", summary="获取所有项目信息")
def get_all_projects(db: Session = Depends(get_db)):
    db_projects = get_project_all(db)
    # 增加判断SQL查询是否成功
    if not db_projects:
        return {"message": "未找到任何项目信息"}
    return {"data": db_projects, "message": "成功查询到所有项目信息"}


@project.get("/list/{project_id}", summary="根据项目ID查询")
def get_projects_id(project_id, db: Session = Depends(get_db)):
    db_project = get_project(db, project_id)
    return {"data": db_project, "message": "根据项目ID查询成功"}


@project.post('/addProject', summary="新增项目")
def create_projects(projects: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = create_project(db, projects)
    return {"data": db_project, "message": "新增项目信息成功"}
