from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from db import engine, Base

class School(Base):
    __tablename__ = "schools"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Primary key
    school = Column('school', String)
    school_count = Column('school_count', Integer)
    repeat_faculty = Column('repeat_faculty', Integer, nullable=True)
    unique_faculty = Column('unique_faculty', Integer, nullable=True)
 
class Department(Base):
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    __tablename__ = "departments"
    department = Column('department', String)
    course = Column('course', String)