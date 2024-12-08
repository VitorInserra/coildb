from models.gradstudent_recipient import GradStudentRecipient
from sqlalchemy.orm import Session
from sqlalchemy import func
import logging
from db import SessionLocal
from models.schemas.gradstudent_recipient import GradStudentRecipientModel
from models.schemas.base_m import LargestIdResponse
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from typing import List
from dependencies import get_current_username


class GradStudentRecipientResource:
    def __init__(self):
        self.router = APIRouter()
        self.router = APIRouter(
            prefix="/gradstudent-recipient", tags=["GradStudentResource"]
        )

    def get_router(self):

        @self.router.get(
            "/gradstudent-recipient/", response_model=List[GradStudentRecipientModel]
        )
        async def get_gradstudent(db: Session = Depends(get_db)):
            gradstudent = db.query(GradStudentRecipient)
            return [
                GradStudentRecipientModel.from_orm(student) for student in gradstudent
            ]

        @self.router.post(
            "/gradstudent-recipient/", response_model=GradStudentRecipientModel
        )
        async def create_gradstudent(
            gradstudent: GradStudentRecipientModel,
            db: Session = Depends(get_db),
            username: str = Depends(get_current_username),
        ):
            db_student = GradStudentRecipient(**gradstudent.dict())
            db.add(db_student)
            db.commit()
            db.refresh(db_student)
            return db_student
        
        @self.router.delete("/delete-recipient/{id}", response_model=GradStudentRecipientModel)
        async def delete_gradstudent_recipient(id: int, db: Session = Depends(get_db)):
            db_student = db.query(GradStudentRecipient).filter(GradStudentRecipient.id == id).first()
            if not db_student:
                raise HTTPException(status_code=404, detail="GradStudentRecipient not found")
            db.delete(db_student)
            db.commit()
            return db_student

        @self.router.put("/update-recipient/", response_model=GradStudentRecipientModel)
        async def update_gradstudent_recipient(
            updated_data: GradStudentRecipientModel,
            username: str = Depends(get_current_username),
            db: Session = Depends(get_db),
        ):
            try:
                db_student = db.query(GradStudentRecipient).filter_by(
                    id=updated_data.id,
                ).first()
                if not db_student:
                    raise HTTPException(status_code=404, detail="Recipient not found")

                for key, value in updated_data.dict().items():
                    if hasattr(db_student, key) and value is not None:
                        setattr(db_student, key, value)

                db.commit()
                db.refresh(db_student)
                return db_student
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
        
        @self.router.get("/largest-id", response_model=LargestIdResponse)
        async def get_largest_id(db: Session = Depends(get_db)):
            largest_id = db.query(func.max(GradStudentRecipient.id)).scalar()
            if largest_id is None:
                return {"largest_id": 0}
            return {"largest_id": largest_id}


        return self.router
