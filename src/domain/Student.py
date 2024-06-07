""""Student Domain Entity"""
from sqlalchemy import Column, Integer, String
from src.database import DomainBase

class Student(DomainBase):
    """"Student Domain Entity"""
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    dni = Column(Integer, nullable=True)
    current_course = Column(String(100), nullable=True)
