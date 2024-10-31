from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from sqlalchemy.ext.declarative import declarative_base
from db import engine  # Import engine from db.py

# Define the base class for models
Base = declarative_base()

class School(base):
    __tablename__ = "school_count"
    id = Column(Integer, primary_key=True, index=True)
    school_name = Column(String)
    school_count = Column(Integer)
    repeat_faculty = Column(Integer)
    unique = Column(Integer)
 
class Department(base):
    __tablename__ = "department_list"
    id = Column(Integer, primary_key=True, index=True)
    department = Column(String)
    courses = Column(ARRAY(String))