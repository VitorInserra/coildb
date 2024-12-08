from typing import List
from models.school_dept import School, Department
from sqlalchemy import func
from sqlalchemy.orm import Session
from db import SessionLocal
from models.schemas.school_dept import SchoolModel, DepartmentModel
from models.schemas.base_m import LargestIdResponse
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
# from models.coil_base import CoilBase

class SchoolDeptResource:
    def __init__(self):
        self.router = APIRouter()
        self.router = APIRouter(prefix="/school-dept", tags=["SchoolDeptResource"])

    def get_router(self):

        @self.router.get("/schools_table", response_model=List[SchoolModel])  # Use List to return multiple records
        async def get_schools(db: Session = Depends(get_db)):
            result = db.query(School).all()  # Use .all() to get all records
            if result:
                return result
            else:
                return {"message": "No schools found"}
            
        @self.router.get("/departments_table", response_model=List[DepartmentModel])  # Use List to return multiple records
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
        async def create_school(school: SchoolModel, db: Session = Depends(get_db)):
            db_school = School(**dict(school))
            db.add(db_school)
            db.commit()
            db.refresh(db_school)
            return db_school
        
        @self.router.get("/largest-id/school", response_model=LargestIdResponse)
        async def get_largest_id_school(db: Session = Depends(get_db)):
            largest_id = db.query(func.max(School.id)).scalar()
            if largest_id is None:
                return {"largest_id": 0}
            return {"largest_id": largest_id}
        
        @self.router.get("/largest-id/department", response_model=LargestIdResponse)
        async def get_largest_id_department(db: Session = Depends(get_db)):
            largest_id = db.query(func.max(Department.id)).scalar()
            if largest_id is None:
                return {"largest_id": 0}
            return {"largest_id": largest_id}
        
        @self.router.delete("/delete-school/{id}", response_model=SchoolModel)
        async def delete_school(id: int, db: Session = Depends(get_db)):
            db_school = db.query(School).filter(School.id == id).first()
            if not db_school:
                raise HTTPException(status_code=404, detail="School not found")
            db.delete(db_school)
            db.commit()
            return db_school
        
        @self.router.delete("/delete-department/{id}", response_model=DepartmentModel)
        async def delete_department(id: int, db: Session = Depends(get_db)):
            db_department = db.query(Department).filter(Department.id == id).first()
            if not db_department:
                raise HTTPException(status_code=404, detail="Department not found")
            db.delete(db_department)
            db.commit()
            return db_department

        return self.router