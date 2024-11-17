from models.gradstudent_recipient import GradStudentRecipient
from sqlalchemy.orm import Session
from db import SessionLocal
from models.schemas.gradstudent_recipient import GradStudentRecipientModel
from fastapi import APIRouter, Depends
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


        return self.router