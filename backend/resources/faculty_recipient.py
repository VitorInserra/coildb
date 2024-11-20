from backend.models.faculty_recipient import FacultyRecipient
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models.schemas.faculty_recipient import FacultyRecipientModel
from fastapi import APIRouter, Depends
# from models.coil_base import CoilBase

class FacultyRecipientResource:
    def __init__(self, db: Session):
        self.router = APIRouter()

    def get_router(self):
        def get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        @self.router.get("/faculty-recipient/{faculty_id}", response_model=FacultyRecipientModel)
        async def get_faculty_recipient(faculty_id: int, db: Session = Depends(get_db)):
            return db.query(FacultyRecipient).filter(FacultyRecipient.id == faculty_id).first()

        @self.router.post("/faculty-recipient/", response_model=FacultyRecipientModel)
        async def create_faculty_recipient(faculty: FacultyRecipientModel, db: Session = Depends(get_db)):
            db_faculty = FacultyRecipient(**faculty.dict())
            db.add(db_faculty)
            db.commit()
            db.refresh(db_faculty)
            return db_faculty



        return self.router