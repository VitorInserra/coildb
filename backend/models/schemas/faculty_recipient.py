from pydantic import BaseModel

class FacultyRecipientModel(BaseModel):
    last_name: str
    first_name: str
    email: str
    semester_taught: str
    school: str
    department: str
    course_number: str
    sections: int
    total_sections_taught: int
    co_taught: str
    repeat_course: str
    joint_course: str
    quarter: str
    estimated_unc_students: int
    estimated_partner_students: int
    unc_students_fdoc_count: int
    unc_students_ldoc_count: int
    partner_institution1: str
    partner_country1: str
    partner_faculty1: str
    partner_institution2: str
    partner_country2: str
    partner_faculty2: str
    award_date: str 
    graduate_student: str
    faculty_amount_rewarded: int
    graduate_award_student_amount: int
    repeat_award: bool
    repeat_award_criteria: str
    coil_champions: str
    notes: str
    partner_region: str

    class Config:
        orm_mode = True