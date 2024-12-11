from fastapi.middleware.cors import CORSMiddleware
from db import get_db
from db import get_db
from resources.coil_base import CoilBase
from resources.compiled_quantitative_data import CompiledDataResource
from resources.faculty_recipient import FacultyRecipientResource
from resources.gradstudent_recipient import GradStudentRecipientResource
from resources.school_dept import SchoolDeptResource
from resources.starred_report import StarredReportResource
from resources.key_stats import KeyStatisticsResource
import uvicorn
from api import app#, create_auth_middleware
from services.school_dept_compile import update_faculty_counts

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

app.include_router(CoilBase().get_router())
app.include_router(CompiledDataResource().get_router())
app.include_router(FacultyRecipientResource().get_router())
app.include_router(GradStudentRecipientResource().get_router())
app.include_router(SchoolDeptResource().get_router())
app.include_router(StarredReportResource().get_router())
app.include_router(KeyStatisticsResource().get_router())

@app.on_event("startup")
async def on_startup():
   # Directly use get_db() to fetch the session
   db = next(get_db())  # Get the database session
   try:
       # You can call your function here, for example update_faculty_counts(db)
       update_faculty_counts(db)
   finally:
       db.close()  # Close the session after use


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)

