from pydantic import BaseModel

class GradStudentRecipientModel(BaseModel):
    semester_taught = str
    last_name = str
    first_name = str
    faculty_supervisor = str
    school = str
    department = str
    course_number = str
    unc_course_name = str
    partner_institution = str
    award = int
    class Config:
        orm_mode = True