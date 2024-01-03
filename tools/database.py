# 1.导入 SQLAlchemy 部件
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 2.为 SQLAlchemy 定义数据库 URL地址
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@localhost:3306/fast_api?charset=utf8mb4"

# 3.创建 SQLAlchemy 引擎
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
# 4.创建一个SessionLocal 数据库会话
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 5.创建一个Base类
Base = declarative_base()
