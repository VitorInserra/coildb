from models.compiled_quantitative_data import CompiledQuantitativeData
from sqlalchemy.orm import Session
from db import get_db
from models.schemas.compiled_quantitative_data import CompiledDataModel
from fastapi import APIRouter, Depends
import json
# from models.coil_base import CoilBase

class CompiledDataResource:
    def __init__(self):
        self.router = APIRouter(prefix="/compiled-data", tags=["CompiledDataResource"])

    def get_router(self):
        @self.router.get("/get-data/{faculty_id}", response_model=CompiledDataModel)
        async def get_compiled_data(compiled_id: int, db: Session = Depends(get_db)):
            return db.query(CompiledQuantitativeData).filter(CompiledQuantitativeData.id == compiled_id).first()

        @self.router.post("/add-data/", response_model=CompiledDataModel)
        async def create_compiled_data(data: CompiledDataModel, db: Session = Depends(get_db)):
            db_compiled = CompiledQuantitativeData()
            db.add(db_compiled)
            db.commit()
            db.refresh(db_compiled)
            return db_compiled


        return self.router