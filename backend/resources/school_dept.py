from typing import List
from models.school_dept import School, Department
from sqlalchemy.orm import Session
from db import SessionLocal
from models.schemas.school_dept import SchoolModel, DepartmentModel
from fastapi import APIRouter, Depends
from db import get_db
from dependencies import get_current_username


class SchoolDeptResource:
    def __init__(self):
        self.router = APIRouter()
        self.router = APIRouter(prefix="/school-dept", tags=["SchoolDeptResource"])

    def get_router(self):

        @self.router.get(
            "/schools_table", response_model=List[SchoolModel]
        )  # Use List to return multiple records
        async def get_schools(db: Session = Depends(get_db)):
            result = db.query(School).all()  # Use .all() to get all records
            if result:
                return result
            else:
                return {"message": "No schools found"}

        @self.router.get(
            "/departments_table", response_model=List[DepartmentModel]
        )  # Use List to return multiple records
        async def get_departments(db: Session = Depends(get_db)):
            result = db.query(Department).all()  # Use .all() to get all records
            if result:
                return result
            else:
                return {"message": "No departments found"}

        @self.router.get("/schools", response_model=SchoolModel)
        async def get_school(school_id: int, db: Session = Depends(get_db)):
            result = db.query(School).filter(School.id == school_id).first()
            if result:
                return result
            else:
                return {"message": "No matching school found"}

        @self.router.get("/depts", response_model=DepartmentModel)
        async def get_department(department_id: int, db: Session = Depends(get_db)):
            result = db.query(Department).filter(Department.id == department_id).first()
            if result:
                return result
            else:
                return {"message": "No matching department found"}

        @self.router.post("/schools", response_model=SchoolModel)
        async def create_school(
            school: SchoolModel,
            db: Session = Depends(get_db),
            username: str = Depends(get_current_username),
        ):
            db_school = School(**dict(school))
            db.add(db_school)
            db.commit()
            db.refresh(db_school)
            return db_school

        return self.router
