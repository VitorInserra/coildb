from typing import List
from models.school_dept import School, Department
from sqlalchemy.orm import Session
from db import SessionLocal
from models.schemas.school_dept import SchoolModel, DepartmentModel
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
        
        @self.router.put("/update-school/", response_model=SchoolModel)
        async def update_school(updated_data: SchoolModel, db: Session = Depends(get_db)):
            try:
                db_school = db.query(School).filter_by(
                    id=updated_data.id,
                ).first()
                if not db_school:
                    raise HTTPException(status_code=404, detail="Recipient not found")

                for key, value in updated_data.dict().items():
                    if key in {"repeat_faculty", "unique_faculty"}:
                        continue  # Skip these fields
                    if hasattr(db_school, key) and value is not None:
                        setattr(db_school, key, value)

                db.commit()
                db.refresh(db_school)
                return db_school
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")


        return self.router