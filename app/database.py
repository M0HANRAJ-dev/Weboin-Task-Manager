from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

# /tmp works on both Vercel (read-only fs) and local dev
# Override with DATABASE_URL env var for persistent DB (e.g. Postgres)
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:////tmp/test.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
