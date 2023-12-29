from fastapi import APIRouter

testcase = APIRouter()


@testcase.get("/")
async def get_project():
    return {"hello project"}
