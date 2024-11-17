from models.gradstudent_recipient import GradStudentRecipient
from sqlalchemy.orm import Session
from db import SessionLocal
from models.schemas.gradstudent_recipient import GradStudentRecipientModel
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from typing import List
# from models.coil_base import CoilBase

class GradStudentRecipientResource:
    def __init__(self):
        self.router = APIRouter()
        self.router = APIRouter(prefix="/gradstudent-recipient", tags=["GradStudentResource"])

    def get_router(self):

        @self.router.get("/gradstudent-recipient/", response_model=List[GradStudentRecipientModel])
        async def get_gradstudent(db: Session = Depends(get_db)):
            gradstudent = db.query(GradStudentRecipient)
            return [GradStudentRecipientModel.from_orm(student) for student in gradstudent]


        @self.router.post("/gradstudent-recipient/", response_model=GradStudentRecipientModel)
        async def create_gradstudent(gradstudent: GradStudentRecipientModel, db: Session = Depends(get_db)):
            db_student = GradStudentRecipient(**gradstudent.dict())
            db.add(db_student)
            db.commit()
            db.refresh(db_student)
            return db_student
        
        @self.router.delete("/delete-recipient/{last_name}/{first_name}", response_model=GradStudentRecipientModel)
        async def delete_gradstudent_recipient(last_name: str, first_name: str, db: Session = Depends(get_db)):
            matching_student = db.query(GradStudentRecipient).filter(GradStudentRecipient.last_name == last_name, GradStudentRecipient.first_name == first_name).all()
            if not matching_student:
                raise HTTPException(status_code=404, detail="FacultyRecipient not found")
            if len(matching_student) > 1:
                raise HTTPException(status_code=400, detail="Multiple records found for the given faculty name. Please check the database.")
            db_student = matching_student[0]
            db.delete(db_student)
            db.commit()
            return db_student

        return self.router