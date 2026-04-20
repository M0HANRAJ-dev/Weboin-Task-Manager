from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db")
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}

Base = declarative_base()

_engine = None
_SessionLocal = None
_initialized = False

def get_engine():
    global _engine, _SessionLocal
    if _engine is None:
        _engine = create_engine(DATABASE_URL, connect_args=connect_args)
        _SessionLocal = sessionmaker(bind=_engine, autoflush=False, autocommit=False)
    return _engine

def ensure_tables():
    global _initialized
    if not _initialized:
        from app import models  # import here to avoid circular at module level
        Base.metadata.create_all(bind=get_engine())
        _initialized = True

def get_db():
    ensure_tables()
    db = _SessionLocal()
    try:
        yield db
    finally:
        db.close()
