from pydantic import BaseModel

class SchoolModel(BaseModel):
    school = str
    school_count = int
    repeat_faculty = int
    unique_faculty = int
    class Config:
        orm_mode = True

class DepartmentModel(BaseModel):
    department = str
    course = str

    class Config:
        orm_mode = True