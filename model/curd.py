# curd.py
from model.database import SessionLocal


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 所有与数据库相关的增删改查的操作方法
