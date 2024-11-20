from models.faculty_recipient import FacultyRecipient
from sqlalchemy.orm import Session
from db import SessionLocal
from db import get_db
from models.schemas.faculty_recipient import FacultyRecipientModel
from fastapi import APIRouter, Depends, HTTPException
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
    
        @self.router.delete("/delete-recipient/{last_name}/{first_name}", response_model=FacultyRecipientModel)
        async def delete_faculty_recipient(last_name: str, first_name: str, db: Session = Depends(get_db)):
            matching_faculty = db.query(FacultyRecipient).filter(FacultyRecipient.last_name == last_name, FacultyRecipient.first_name == first_name).all()
            if not matching_faculty:
                raise HTTPException(status_code=404, detail="FacultyRecipient not found")
            if len(matching_faculty) > 1:
                raise HTTPException(status_code=400, detail="Multiple records found for the given faculty name. Please check the database.")
            db_faculty = matching_faculty[0]
            db.delete(db_faculty)
            db.commit()
            return db_faculty
        

        return self.router