# schemas.py

from pydantic import BaseModel


class Project(BaseModel):
    id: int
    project_name: str
    Project_creator: str
    Project_creation_time: str
