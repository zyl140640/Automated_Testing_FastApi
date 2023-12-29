from fastapi import APIRouter

teststep = APIRouter()


@teststep.get("/")
async def get_project():
    return {"hello project"}
