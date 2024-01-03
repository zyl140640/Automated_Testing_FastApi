from sqlalchemy.orm import Session

from tools.database import SessionLocal


# Dependency
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
