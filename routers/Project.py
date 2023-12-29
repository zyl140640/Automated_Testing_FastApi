# 接口层  curd调用models 接口调用 schemas 和 curd  schemas接口请求方法（）内， curd在请求体内 也就是 ：下面
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from model import schemas
from model.curd import get_project, get_db, create_project, get_project_all, update_project, delete_project

project = APIRouter()


@project.get("/list", summary="获取所有项目信息")
def get_all_projects(db: Session = Depends(get_db)):
    db_projects = get_project_all(db)
    # 增加判断SQL查询是否成功
    if not db_projects:
        return {"message": "未找到任何项目信息"}
    return {"data": db_projects, "message": "成功查询到所有项目信息"}


@project.get("/list/{project_id}", summary="根据项目ID查询相应信息")
def get_projects_id(project_id, db: Session = Depends(get_db)):
    db_project = get_project(db, project_id)
    if db_project:
        return {"data": db_project, "message": "根据项目ID查询成功"}
    else:
        return {"message": "找不到该ID项目"}


@project.post('/addProject', summary="新增项目信息")
def create_projects(projects: schemas.ProjectCreate, db: Session = Depends(get_db)):
    db_project = create_project(db, projects)
    if db_project:
        return {"data": db_project, "message": "新增项目信息成功"}
    else:
        return {"message": "新增项目失败"}


@project.put('/updateProject', summary="修改项目信息")
def update_projects(projects: schemas.ProjectUpdate, db: Session = Depends(get_db)):
    db_project = update_project(db, projects)
    if db_project:
        return {"data": db_project, "message": "项目信息修改成功"}
    else:
        return {"message": "找不到要修改的项目"}


@project.delete('/deleteProject/{project_id}', summary="删除项目")
def delete_project_endpoint(project_id: int, db: Session = Depends(get_db)):
    success = delete_project(db, project_id)
    if success:
        return {"message": f"项目ID为 {project_id} 的项目已成功删除"}
    else:
        return {"message": f"找不到项目ID为 {project_id} 的项目"}
