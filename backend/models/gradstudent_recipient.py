from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from sqlalchemy.ext.declarative import declarative_base
from db import engine  # Import engine from db.py

# Define the base class for models
Base = declarative_base()

class GradStudentRecipient(Base):
    __tablename__ = "gradstudent_recipient"
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    semester_taught = Column(String)
    last_name = Column(String)
    first_name = Column(String)
    faculty_supervisor = Column(String)
    school = Column(String)
    department = Column(String)
    course_number = Column(String)
    unc_course_name = Column(String)
    partner_institution = Column(String)
    award = Column(Integer)

Base.metadata.create_all(bind=engine)