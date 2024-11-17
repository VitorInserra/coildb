from models.faculty_recipient import FacultyRecipient
from sqlalchemy.orm import Session
from db import SessionLocal
from db import get_db
from models.schemas.faculty_recipient import FacultyRecipientModel
from fastapi import APIRouter, Depends
from typing import List, Union
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
        async def create_faculty_recipient(faculty: FacultyRecipientModel, db: Session = Depends(get_db)):
            db_faculty = FacultyRecipient(**faculty.dict())
            db.add(db_faculty)
            db.commit()
            db.refresh(db_faculty)
            return db_faculty



        return self.router