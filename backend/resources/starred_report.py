from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from db import get_db
from models.starred_report import StarredReport
from models.schemas.starred_report import StarredReportModel
from dependencies import get_current_username

class StarredReportResource:
    def __init__(self):
        self.router = APIRouter(prefix="/starred-reports", tags=["StarredReportResource"])

    def get_router(self):
        @self.router.post("/", response_model=StarredReportModel)
        async def create_starred_report(report: StarredReportModel, db: Session = Depends(get_db)):
            # Check if a report with the same title already exists
            existing_report = db.query(StarredReport).filter(StarredReport.title == report.title).first()
            if existing_report:
                raise HTTPException(status_code=400, detail="Starred report with this title already exists")

            new_report = StarredReport(**report.dict())
            db.add(new_report)
            db.commit()
            db.refresh(new_report)
            return new_report

        @self.router.get("/", response_model=List[StarredReportModel])
        async def get_all_starred_reports(db: Session = Depends(get_db)):
            reports = db.query(StarredReport).all()
            return reports

        @self.router.get("/{title}", response_model=StarredReportModel)
        async def get_starred_report(title: str, db: Session = Depends(get_db)):
            report = db.query(StarredReport).filter(StarredReport.title == title).first()
            if not report:
                raise HTTPException(status_code=404, detail="Starred report not found")
            return report

        return self.router
