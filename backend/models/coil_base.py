# models.py
from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from db import engine, Base


class CoilBase(Base):
    __tablename__ = "coil_base"  

    id = Column(Integer, primary_key=True, index=True) 

Base.metadata.create_all(bind=engine)