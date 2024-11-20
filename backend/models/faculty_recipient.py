from sqlalchemy import Column, Integer, String, Boolean, ARRAY, TIMESTAMP, Float, func, Date
from sqlalchemy.ext.declarative import declarative_base
from db import engine  # Import engine from db.py

# Define the base class for models
Base = declarative_base()

class FacultyRecipient(Base):
    __tablename__ = "faculty"
    #id = Column(Integer, primary_key=True, index=True)  # Primary key
    last_name = Column('Last Name', String, nullable=False, primary_key=True, index=False)  
    first_name = Column('First Name', String, nullable=False)  
    email = Column('Email', String, unique=True, nullable=False)  
    semester_taught = Column('Semester Taught', String, nullable=False)  
    school = Column('School', String)  
    department = Column('Department', String)
    course_name = Column('Course Name', String)  
    course_number = Column('Course Number', String) 
    sections = Column('Sections', Integer)  
    total_sections_taught = Column('Total # Sections Taught', Integer) 
    course_title = Column('Course Title', String, nullable=False)
    co_taught_semester = Column('Co-taught Semester', String)
    co_taught_year = Column('Co-taught Year', Integer)
    repeat_course_semester = Column('Repeat Course Semester', String) 
    repeat_course_year = Column('Repeat Course Year', Integer)
    joint_course = Column('Joint - course', String) 
    quarter = Column('Quarter', String)  
    estimated_unc_students = Column('Estimated UNC Students ', Integer) 
    estimated_partner_students = Column('Estimated Partner Students', Integer)  
    unc_students_fdoc_count = Column('Enrolled UNC Students (FDOC)', Integer)  
    unc_students_ldoc_count = Column('Enrolled UNC Students (LDOC)', Integer)  
    partner_institution1 = Column('Partner Institution 1', String) 
    partner_country1 = Column('Partner Country 1', String)  
    partner_faculty1 = Column('Partner Faculty 1', String) 
    partner_institution2 = Column('Partner Institution 2', String) 
    partner_country2 = Column('Partner Country 2', String)  
    partner_faculty2 = Column('Partner Faculty 2', String)
    credit = Column('EE/HI Credit', String)  
    award_date = Column('Award Date', Date)  
    graduate_student = Column('Graduate Student', String) 
    faculty_amount_rewarded = Column('Faculty Amount Awarded', Integer) 
    graduate_award_student_amount = Column('Graduate Student Award Amount ', Integer) 
    repeat_award = Column('Repeat Award ', String)  
    repeat_award_criteria = Column('Repeat Award Criteria ', String)  
    coil_champions = Column('COIL Champion', String)  
    notes = Column('Notes', String)  # Additional notes
    partner_region = Column('Partner region', String)
    cancelled = Column('Cancelled', Boolean)

Base.metadata.create_all(bind=engine)