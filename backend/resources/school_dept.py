from typing import List
from models.school_dept import School, Department
from sqlalchemy import func
from sqlalchemy.orm import Session
from db import SessionLocal
from models.schemas.school_dept import SchoolCreateModel, SchoolModel, DepartmentModel
from models.schemas.base_m import LargestIdResponse
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from dependencies import get_current_username
from services.school_dept_compile import update_faculty_counts


class SchoolDeptResource:
    def __init__(self):
        self.router = APIRouter()
        self.router = APIRouter(prefix="/school-dept", tags=["SchoolDeptResource"])

    def get_router(self):

        @self.router.get(
            "/schools_table", response_model=List[SchoolModel]
        )  # Use List to return multiple records
        async def get_schools(db: Session = Depends(get_db)):
            result = db.query(School).order_by(School.id).all()  # Use .all() to get all records
            if result:
                return result
            else:
                return {"message": "No schools found"}

        @self.router.get(
            "/departments_table", response_model=List[DepartmentModel]
        )  # Use List to return multiple records
        async def get_departments(db: Session = Depends(get_db)):
            result = db.query(Department).order_by(Department.id).all()  # Use .all() to get all records
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

        @self.router.post("/schools", response_model=SchoolCreateModel)
        async def create_school(
            school: SchoolCreateModel,
            db: Session = Depends(get_db),
        ):
            db_school = School(**dict(school))
            db.add(db_school)
            db.commit()
            db.refresh(db_school)
            update_faculty_counts(db)
            return db_school
        
        @self.router.post("/department", response_model=DepartmentModel)
        async def create_department(
            department: DepartmentModel,
            db: Session = Depends(get_db)
        ):
            db_department = Department(**dict(department))
            db.add(db_department)
            db.commit()
            db.refresh(db_department)
            return db_department
        
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
        
        @self.router.delete("/delete-school/name/{name}", response_model=SchoolModel)
        async def delete_school_name(name: str, db: Session = Depends(get_db)):
            db_school = db.query(School).filter(School.school == name).first()
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
        
        @self.router.put("/update-school/", response_model=SchoolModel)
        async def update_school(
            updated_data: SchoolModel,
            db: Session = Depends(get_db),
        ):
            try:
                db_school = db.query(School).filter_by(
                    id=updated_data.id,
                ).first()
                if not db_school:
                    raise HTTPException(status_code=404, detail="School not found")

                for key, value in updated_data.dict().items():
                    if hasattr(db_school, key) and value is not None:
                        setattr(db_school, key, value)

                db.commit()
                db.refresh(db_school)
                return db_school
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
            
        @self.router.put("/update-department/", response_model=DepartmentModel)
        async def update_department(
            updated_data: DepartmentModel,
            db: Session = Depends(get_db),
        ):
            try:
                db_department = db.query(Department).filter_by(
                    id=updated_data.id,
                ).first()
                if not db_department:
                    raise HTTPException(status_code=404, detail="Department not found")

                for key, value in updated_data.dict().items():
                    if hasattr(db_department, key) and value is not None:
                        setattr(db_department, key, value)

                db.commit()
                db.refresh(db_department)
                return db_department
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

        return self.router
    