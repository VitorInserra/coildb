from backend.models.compiled_quantitative_data import CompiledQuantitativeData
from sqlalchemy.orm import Session
from backend.db import get_db
from backend.models.schemas.compiled_quantitative_data import CompiledDataModel
from fastapi import APIRouter, Depends
# from models.coil_base import CoilBase

class CompiledDataResource:
    def __init__(self, db: Session):
        self.router = APIRouter()

        @self.router.get("/compiled-quantitative-data/{faculty_id}", response_model=CompiledDataModel)
        async def get_compiled_data(compiled_id: int, db: Session = Depends(get_db)):
            return db.query(CompiledQuantitativeData).filter(CompiledQuantitativeData.id == compiled_id).first()

        @self.router.post("/compiled-quantitative-data/", response_model=CompiledDataModel)
        async def create_compiled_data(data: CompiledDataModel, db: Session = Depends(get_db)):
            db_compiled = CompiledQuantitativeData(**dict(data))
            db.add(db_compiled)
            db.commit()
            db.refresh(db_compiled)
            return db_compiled



        return self.router