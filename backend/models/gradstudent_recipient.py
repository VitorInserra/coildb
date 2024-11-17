from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from sqlalchemy.ext.declarative import declarative_base
from db import engine  # Import engine from db.py

# Define the base class for models
Base = declarative_base()

class GradStudentRecipient(Base):
    __tablename__ = "grad_student"
    semester_taught = Column('Semester Taught', String)
    year_taught = Column('Year Taught', Integer)
    last_name = Column('Last Name', String, primary_key=True, index=False)#Primary key
    first_name = Column('First Name', String)
    faculty_supervisor = Column('Faculty Supervisor', String)
    school = Column('School', String)
    department = Column('Department', String)
    course= Column('Course', String)
    number = Column('Number', String)
    unc_course_name = Column('UNC Course Name', String)
    #partner_institution = Column(String)
    #award = Column(Integer)

Base.metadata.create_all(bind=engine)