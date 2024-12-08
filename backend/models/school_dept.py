from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from db import engine, Base

class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    school = Column(String)
    school_count = Column(Integer)
    repeat_faculty = Column(Integer, nullable=True)
    unique_faculty = Column(Integer, nullable=True)
 
class Department(Base):
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    __tablename__ = "departments"
    department = Column(String)
    course = Column(String)