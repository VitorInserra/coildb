from backend.models.gradstudent_recipient import GradStudentRecipient
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models.schemas.gradstudent_recipient import GradStudentRecipientModel
from fastapi import APIRouter, Depends
# from models.coil_base import CoilBase

class GradStudentRecipientResource:
    def __init__(self, db: Session):
        self.router = APIRouter()

    def get_router(self):

        def get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()

        @self.router.get("/gradstudent-recipient/{gradstudent_id}", response_model=GradStudentRecipientModel)
        async def get_gradstudent(gradstudent_id: int, db: Session = Depends(get_db)):
            return db.query(GradStudentRecipient).filter(GradStudentRecipient.id == gradstudent_id).first()


        @self.router.post("/gradstudent-recipient/", response_model=GradStudentRecipientModel)
        async def create_gradstudent(gradstudent: GradStudentRecipientModel, db: Session = Depends(get_db)):
            db_student = GradStudentRecipient(**gradstudent.dict())
            db.add(db_student)
            db.commit()
            db.refresh(db_student)
            return db_student


        return self.router