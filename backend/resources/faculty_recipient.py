from models.faculty_recipient import FacultyRecipient
from sqlalchemy.orm import Session
from sqlalchemy import func
from db import SessionLocal
from db import get_db
from models.schemas.faculty_recipient import FacultyRecipientModel
from models.schemas.base_m import LargestIdResponse
from fastapi import APIRouter, Depends, HTTPException
from typing import List, Union
from dependencies import get_current_username
# from models.coil_base import CoilBase

class FacultyRecipientResource:
    def __init__(self):
        self.router = APIRouter(prefix="/faculty-recipient", tags=["FacultyRecipientResource"])

    def get_router(self):
        @self.router.get("/get-recipient", response_model=List[FacultyRecipientModel])
        async def get_faculty_table(db: Session = Depends(get_db)):
            faculty_list = db.query(FacultyRecipient)
            return [FacultyRecipientModel.from_orm(faculty) for faculty in faculty_list]

        @self.router.get("/get-recipient/{column}/{input}/", response_model=Union[FacultyRecipientModel, List[FacultyRecipientModel]])
        async def get_faculty_recipient(column: str, input: str, db: Session = Depends(get_db)):
            query = db.query(FacultyRecipient).filter(getattr(FacultyRecipient, column) == input)
            result = query.all()
            if result:
                return result
            else:
                return {"message": "No matching faculty recipient found"}

        @self.router.post("/post-recipient/", response_model=FacultyRecipientModel)
        async def create_faculty_recipient(faculty: FacultyRecipientModel, db: Session = Depends(get_db), username: str = Depends(get_current_username)):
            db_faculty = FacultyRecipient(**faculty.dict())
            db.add(db_faculty)
            db.commit()
            db.refresh(db_faculty)
            return db_faculty
        
        @self.router.put("/update-recipient/", response_model=FacultyRecipientModel)
        async def update_faculty_recipient(updated_data: FacultyRecipientModel, db: Session = Depends(get_db)):
            try:
                db_student = db.query(FacultyRecipient).filter_by(
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
            largest_id = db.query(func.max(FacultyRecipient.id)).scalar()
            if largest_id is None:
                return {"largest_id": 0}
            return {"largest_id": largest_id}
        
        @self.router.delete("/delete-recipient/{id}", response_model=FacultyRecipientModel)
        async def delete_faculty_recipient(id: int, db: Session = Depends(get_db)):
            db_student = db.query(FacultyRecipient).filter(FacultyRecipient.id == id).first()
            if not db_student:
                raise HTTPException(status_code=404, detail="FacultyRecipient not found")
            db.delete(db_student)
            db.commit()
            return db_faculty
        
        @self.router.put("/update-recipient/", response_model=FacultyRecipientModel)
        async def update_faculty_recipient(updated_data: FacultyRecipientModel, db: Session = Depends(get_db)):
            try:
                db_faculty = db.query(FacultyRecipient).filter_by(
                    id=updated_data.id,
                ).first()
                if not db_faculty:
                    raise HTTPException(status_code=404, detail="Recipient not found")

                for key, value in updated_data.dict().items():
                    if hasattr(db_faculty, key) and value is not None:
                        setattr(db_faculty, key, value)

                db.commit()
                db.refresh(db_faculty)
                return db_faculty
            except Exception as e:
                raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
        


        return self.router