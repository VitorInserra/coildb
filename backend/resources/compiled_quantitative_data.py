from backend.models.compiled_quantitative_data import CompiledQuantitativeData
from sqlalchemy.orm import Session
from backend.db import SessionLocal
from backend.models.schemas.compiled_quantitative_data import CompiledDataModel
from fastapi import APIRouter, Depends
# from models.coil_base import CoilBase

class CompiledDataResource:
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
        @self.router.get("/compiled_quantitative_data/{faculty_id}", response_model=CompiledDataModel)
        async def get_compiled_data(compiled_id: int, db: Session = Depends(get_db)):
            return db.query(CompiledQuantitativeData).filter(CompiledQuantitativeData.id == compiled_id).first()

        # Sample POST endpoint
        @self.router.post("/compiled_quantitative_data/", response_model=CompiledDataModel)
        async def create_compiled_data(data: CompiledDataModel, db: Session = Depends(get_db)):
            db_compiled = CompiledQuantitativeData(**data.dict())
            db.add(db_compiled)
            db.commit()
            db.refresh(db_compiled)
            return db_compiled

        # Add more endpoints here as needed

        return self.router