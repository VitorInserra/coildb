from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import SessionLocal
from db import get_db
from sqlalchemy import func
from models.faculty_recipient import FacultyRecipient
from models.school_dept import School

from models.schemas.key_stats import KeyStatsResponse

class KeyStatisticsResource:
    def __init__(self):
        self.router = APIRouter(prefix="/key-stats", tags=["KeyStatisticsResource"])

    def get_router(self):
        
        @self.router.get("/", response_model=KeyStatsResponse)
        async def get_key_statistics(db: Session = Depends(get_db)):
            try:
                # Example queries for statistics
                departments_participating = db.query(func.count(func.distinct(FacultyRecipient.department))).scalar()
                courses_available = db.query(func.count(func.distinct(FacultyRecipient.course_title))).scalar()
                participating_schools = db.query(func.sum(School.school_count)).scalar()
                students_enrolled = db.query(func.sum(FacultyRecipient.unc_students_ldoc_count)).scalar()

                return {
                    "departments_participating": departments_participating,
                    "courses_available": courses_available,
                    "participating_schools": participating_schools,
                    "students_enrolled": students_enrolled,
                }
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

        return self.router
