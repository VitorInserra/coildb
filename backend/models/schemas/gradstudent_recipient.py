from pydantic import BaseModel
from typing import Optional

class GradStudentRecipientModel(BaseModel):
    semester_taught: Optional[str] = None
    year_taught: Optional[int] = None
    last_name: Optional[str] = None
    first_name: Optional[str] = None
    faculty_supervisor: Optional[str] = None
    school: Optional[str] = None
    department: Optional[str] = None
    course: Optional[str] = None
    number: Optional[str] = None
    unc_course_name: Optional[str] = None
    partner_institution: Optional[str] = None
    award: Optional[int] = None
    class Config:
        orm_mode = True
        from_attributes=True