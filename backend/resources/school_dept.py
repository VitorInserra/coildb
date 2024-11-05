from backend.models.school_dept import School, Department
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models.schemas.school_dept import SchoolModel, DepartmentModel
from fastapi import APIRouter, Depends
# from models.coil_base import CoilBase

class SchoolDeptResource:
    def __init__(self, db: Session):
        self.router = APIRouter()

    def get_router(self):
        # Dependency to get the database session
        def get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        # Sample GET endpoint
        @self.router.get("/school_dept/schools", response_model=SchoolModel)
        async def get_schools(school_id: int, db: Session = Depends(get_db)):
            return db.query(School).filter(School.id == school_id).first()
          # Sample GET endpoint

        @self.router.get("/school_dept/depts", response_model=DepartmentModel)
        async def get_departments(department_id: int, db: Session = Depends(get_db)):
            return db.query(Department).filter(Department.id == department_id).first()

        # Sample POST endpoint
        @self.router.post("/faculty_recipient/schools", response_model=SchoolModel)
        async def create_school(school: SchoolModel, db: Session = Depends(get_db)):
            db_school = School(**school.dict())
            db.add(db_school)
            db.commit()
            db.refresh(db_school)
            return db_school

        # Add more endpoints here as needed

        return self.router