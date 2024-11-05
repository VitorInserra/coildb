from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from sqlalchemy.ext.declarative import declarative_base
from db import engine  # Import engine from db.py

# Define the base class for models
Base = declarative_base()

class FacultyRecipient(Base):
    __tablename__ = "faculty_recipient"
    id = Column(Integer, primary_key=True, index=True)  # Primary key
    last_name = Column(String, nullable=False)  
    first_name = Column(String, nullable=False)  
    email = Column(String, unique=True, nullable=False)  
    semester_taught = Column(String)  
    school = Column(String)  
    department = Column(String)  
    course_number = Column(String) 
    sections = Column(Integer)  
    total_sections_taught = Column(Integer) 
    co_taught = Column(String)  
    repeat_course = Column(String) 
    joint_course = Column(String) 
    quarter = Column(String)  
    estimated_unc_students = Column(Integer) 
    estimated_partner_students = Column(Integer)  
    unc_students_fdoc_count = Column(Integer)  
    unc_students_ldoc_count = Column(Integer)  
    partner_institution1 = Column(String) 
    partner_country1 = Column(String)  
    partner_faculty1 = Column(String) 
    partner_institution2 = Column(String) 
    partner_country2 = Column(String)  
    partner_faculty2 = Column(String)  
    award_date = Column(String)  
    graduate_student = Column(String) 
    faculty_amount_rewarded = Column(Integer) 
    graduate_award_student_amount = Column(Integer) 
    repeat_award = Column(bool)  
    repeat_award_criteria = Column(String)  
    coil_champions = Column(String)  
    notes = Column(String)  # Additional notes
    partner_region = Column(String)  

Base.metadata.create_all(bind=engine)