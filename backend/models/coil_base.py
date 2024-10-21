# models.py
from sqlalchemy import Column, Integer, String, ARRAY, TIMESTAMP, Float, func
from sqlalchemy.ext.declarative import declarative_base
from db import engine  # Import engine from db.py

# Define the base class for models
Base = declarative_base()

# Declare the VRDataModel class
class CoilBase(Base):
    __tablename__ = "coil_base"  # Name of the table in the database

    # Define columns
    id = Column(Integer, primary_key=True, index=True)  # Primary key

# Create the table if it doesn't already exist
Base.metadata.create_all(bind=engine)