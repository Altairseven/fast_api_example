"""Database Configuration Module"""
from typing import Annotated
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base

from fastapi import Depends

CON_STRING = "postgresql://postgres:postgres@localhost/fastapidb"

engine = create_engine(CON_STRING)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

DomainBase = declarative_base()

def get_db():
    "Factory for database session"
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

dbContext = Annotated[Session, Depends(get_db)]
