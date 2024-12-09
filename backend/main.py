from fastapi.middleware.cors import CORSMiddleware
from db import get_db
from resources.coil_base import CoilBase
from resources.compiled_quantitative_data import CompiledDataResource
from resources.faculty_recipient import FacultyRecipientResource
from resources.gradstudent_recipient import GradStudentRecipientResource
from resources.school_dept import SchoolDeptResource
from resources.starred_report import StarredReportResource
from resources.key_stats import KeyStatisticsResource
import uvicorn
from api import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

