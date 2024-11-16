from sqlalchemy import Column, Integer, String, Boolean, ARRAY, TIMESTAMP, Float, func
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
    semester_taught = Column('Semester Taught', String)  
    school = Column('School', String)  
    department = Column('Department', String)  
    course_number = Column('Course Number', String) #in database, cnumber was split into name and number
    sections = Column('Sections', Integer)  
    total_sections_taught = Column('Total # Sections Taught', Integer) 
    co_taught = Column('Co-taught Semester', String) #missing co-taught year in database  
    repeat_course = Column('Repeat Course Semester', String) #missing repeat course year
    joint_course = Column('Joint - course', String) 
    quarter = Column('Quarter', String)  
    estimated_unc_students = Column('Estimated UNC Students ', Integer) 
    estimated_partner_students = Column('Estimated Partner Students', Integer)  
    unc_students_fdoc_count = Column('Enrolled UNC Students (FDOC)', Integer)  

    #unc_students_ldoc_count = Column(Integer)  
    #partner_institution1 = Column(String) 
    #partner_country1 = Column(String)  
    #partner_faculty1 = Column(String) 
    #partner_institution2 = Column(String) 
    #partner_country2 = Column(String)  
    #partner_faculty2 = Column(String)  
    #award_date = Column(String)  
    #graduate_student = Column(String) 
    #faculty_amount_rewarded = Column(Integer) 
    #graduate_award_student_amount = Column(Integer) 
    #repeat_award = Column(Boolean)  
    #repeat_award_criteria = Column(String)  
    #coil_champions = Column(String)  
    #notes = Column(String)  # Additional notes
    #partner_region = Column(String)

Base.metadata.create_all(bind=engine)