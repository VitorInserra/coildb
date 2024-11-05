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
        # Dependency to get the database session
        def get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        # Sample GET endpoint
        @self.router.get("/faculty_recipient/{faculty_id}", response_model=FacultyRecipientModel)
        async def get_faculty_recipient(faculty_id: int, db: Session = Depends(get_db)):
            return db.query(FacultyRecipient).filter(FacultyRecipient.id == faculty_id).first()

        # Sample POST endpoint
        @self.router.post("/faculty_recipient/", response_model=FacultyRecipientModel)
        async def create_faculty_recipient(faculty: FacultyRecipientModel, db: Session = Depends(get_db)):
            db_faculty = FacultyRecipient(**faculty.dict())
            db.add(db_faculty)
            db.commit()
            db.refresh(db_faculty)
            return db_faculty

        # Add more endpoints here as needed

        return self.router