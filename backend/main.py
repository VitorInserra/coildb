from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from resources.coil_base import CoilBase
from resources.compiled_quantitative_data import CompiledDataResource
from resources.faculty_recipient import FacultyRecipientResource
from resources.gradstudent_recipient import GradStudentRecipientResource
from resources.school_dept import SchoolDeptResource
from resources.starred_report import StarredReportResource

import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(CoilBase().get_router())
app.include_router(CompiledDataResource().get_router())
app.include_router(FacultyRecipientResource().get_router())
app.include_router(GradStudentRecipientResource().get_router())
app.include_router(SchoolDeptResource().get_router())
app.include_router(StarredReportResource().get_router())

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
