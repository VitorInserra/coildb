from pydantic import BaseModel

class SchoolModel(BaseModel):
    school_name = str
    school_count = int
    repeat_faculty = int
    unique = int
    class Config:
        orm_mode = True

class DepartmentModel(BaseModel):
    department = str
    courses = list[str]

    class Config:
        orm_mode = True