from pydantic import BaseModel

class CompiledDataModel(BaseModel):
    semester: str
    offered_course_count = int
    cotaught_courses_count = int
    repeat_courses_count = int
    joint_courses_count = int
    new_courses_count = int
    coil_funding_awards_count = int
    unique_facility_count = int
    grad_award_count = int
    faculty_funding = int
    graduate_funding = int
    estimated_UNC_coil_count = int
    coil_undergrad_fdoc_count = int
    coil_graduate_fdoc_count = int
    coil_students_ldoc_count = int
    coil_undergrad_ldoc_count = int
    coil_graduate_ldoc_count = int
    estimated_partnerstudent_count = int
    partner_country_count = int

    class Config:
        orm_mode = True