from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class FacultyRecipientModel(BaseModel):
    id: int
    last_name:  Optional[str] = None
    first_name:  Optional[str] = None
    email:  Optional[str] = None
    semester_taught:  Optional[str] = None
    school:  Optional[str] = None
    department:  Optional[str] = None
    course_name: Optional[str] = None
    course_number:  Optional[str] = None
    sections: Optional[str] = None
    total_sections_taught: Optional[int] = None
    course_title: Optional[str] = None
    co_taught_semester: Optional[str] = None  # Allow None values
    co_taught_year: Optional[int] = None
    repeat_course_semester: Optional[str] = None  # Allow None values
    repeat_course_year: Optional[int] = None
    joint_course: Optional[str] = None  # Allow None values
    quarter: Optional[str] = None  # Allow None values
    estimated_unc_students: Optional[int] = None
    estimated_partner_students: Optional[int] = None
    unc_students_fdoc_count: Optional[int] = None
    unc_students_ldoc_count: Optional[int] = None
    partner_institution1: Optional[str] = None
    partner_country1: Optional[str] = None
    partner_faculty1: Optional[str] = None
    partner_institution2: Optional[str] = None
    partner_country2: Optional[str] = None
    partner_faculty2: Optional[str] = None
    credit: Optional[str] = None
    award_date: Optional[date] = None
    graduate_student: Optional[str] = None
    faculty_amount_rewarded: Optional[int] = None
    graduate_award_student_amount: Optional[int] = None
    repeat_award: Optional[str] = None
    repeat_award_criteria: Optional[str] = None
    coil_champions: Optional[str] = None
    notes: Optional[str] = None
    partner_region: Optional[str] = None
    cancelled: Optional[bool] = None
    class Config:
        orm_mode = True
        from_attributes = True