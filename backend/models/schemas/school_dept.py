from typing import Optional
from pydantic import BaseModel

class SchoolModel(BaseModel):
    #id: int
    school: str
    school_count: int
    repeat_faculty: Optional[int]
    unique_faculty: Optional[int]
    class Config:
        orm_mode = True


class SchoolCreateModel(BaseModel):
    #id: int
    school: str
    school_count: int
    class Config:
        orm_mode = True

class DepartmentModel(BaseModel):
    #id: int
    department: str
    course: str

    class Config:
        orm_mode = True