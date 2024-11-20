from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from db import engine, Base

class School(Base):
    __tablename__ = "schools"
    school = Column(String)
    school_count = Column(Integer)
    repeat_faculty = Column(Integer)
    unique_faculty = Column(Integer)
 
class Department(Base):
    __tablename__ = "departments"
    department = Column(String)
    course = Column(String)