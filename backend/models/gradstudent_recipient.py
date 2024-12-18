from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from db import engine, Base


class GradStudentRecipient(Base):
    __tablename__ = "grad_student"
    #id = Column(Integer, primary_key=True, index=True, autoincrement=True)  # Primary key
    semester_taught = Column('Semester Taught', String)
    year_taught = Column('Year Taught', Integer)
    last_name = Column('Last Name', String, index=False, primary_key=True)
    first_name = Column('First Name', String)
    faculty_supervisor = Column('Faculty Supervisor', String)
    school = Column('School', String)
    department = Column('Department', String)
    course= Column('Course', String)
    number = Column('Number', String)
    unc_course_name = Column('UNC Course Name', String)
    partner_institution = Column('Partner Institution', String)
    award = Column('Award', Integer)
    email = Column('TA Email', String)
    pid = Column('TA PID', Integer)

Base.metadata.create_all(bind=engine)