from fastapi import APIRouter

project = APIRouter()


@project.get("/")
async def get_project():
    return {"hello project"}
