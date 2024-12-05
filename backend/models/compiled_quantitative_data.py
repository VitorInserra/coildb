from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from db import engine, Base

class CompiledQuantitativeData(Base):
    __tablename__ = "compiled_quantitative_data"
    id = Column(Integer, primary_key=True, index=True) 
    semester = Column(String)
    offered_courses_count = Column(Integer)
    cotaught_courses_count = Column(Integer)
    repeat_courses_count = Column(Integer)
    joint_courses_count = Column(Integer)
    new_courses_count = Column(Integer)
    coil_funding_awards_count = Column(Integer)
    unique_facility_count = Column(Integer)
    grad_award_count = Column(Integer)
    faculty_funding = Column(Integer)
    graduate_funding = Column(Integer)
    estimated_UNC_coil_count = Column(Integer)
    coil_undergrad_fdoc_count = Column(Integer)
    coil_graduate_fdoc_count = Column(Integer)
    coil_students_ldoc_count = Column(Integer)
    coil_undergrad_ldoc_count = Column(Integer)
    coil_graduate_ldoc_count = Column(Integer)
    estimated_partnerstudent_count = Column(Integer)
    partner_country_count = Column(Integer)
    