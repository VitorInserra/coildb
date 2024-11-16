from pydantic import BaseModel
from typing import Optional

class FacultyRecipientModel(BaseModel):
    last_name:  Optional[str] = None
    first_name:  Optional[str] = None
    email:  Optional[str] = None
    semester_taught:  Optional[str] = None
    school:  Optional[str] = None
    department:  Optional[str] = None
    course_number:  Optional[str] = None
    sections: Optional[str] = None
    total_sections_taught: Optional[int] = None
    co_taught: Optional[str] = None  # Allow None values
    repeat_course: Optional[str] = None  # Allow None values
    joint_course: Optional[str] = None  # Allow None values
    quarter: Optional[str] = None  # Allow None values
    estimated_unc_students: Optional[int] = None
    estimated_partner_students: Optional[int] = None
    unc_students_fdoc_count: Optional[int] = None
    #unc_students_ldoc_count: int
    #partner_institution1: str
    #partner_country1: str
    #partner_faculty1: str
    #partner_institution2: str
    #partner_country2: str
    #partner_faculty2: str
    #award_date: str 
    #graduate_student: str
    #faculty_amount_rewarded: int
    #graduate_award_student_amount: int
    #repeat_award: bool
    #repeat_award_criteria: str
    #coil_champions: str
    #notes: str
    #partner_region: str
    class Config:
        orm_mode = True
        from_attributes = True