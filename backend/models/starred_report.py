from sqlalchemy import Column, Integer, String, JSON
from db import Base

class StarredReport(Base):
    __tablename__ = "starred_reports"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    path = Column(String, unique=True, nullable=False)
    filter_settings = Column(JSON, nullable=True)  # Stores filter settings as JSON
