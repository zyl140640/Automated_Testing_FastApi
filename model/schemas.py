# schemas.py  数据校验 用于 请求
from typing import List

from pydantic import BaseModel

from apps.dependencies import current_time


# 请求模型
class Project(BaseModel):
    id: int
    project_name: str
    Project_creator: str
    Project_creation_time: str = current_time()


class ProjectCreate(Project):
    pass

# 响应模型
