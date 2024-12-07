from pydantic import BaseModel

class SchoolModel(BaseModel):
    #id: int
    school: str
    school_count: int
    #repeat_faculty: int
    #unique_faculty: int
    class Config:
        orm_mode = True

class DepartmentModel(BaseModel):
    id: int
    department: str
    course: str

    class Config:
        orm_mode = True