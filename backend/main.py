from fastapi import FastAPI
from resources.coil_base import CoilBase
from resources.compiled_quantitative_data import CompiledDataResource
from resources.faculty_recipient import FacultyRecipientResource
from resources.gradstudent_recipient import GradStudentRecipientResource
# from resources.school_dept import SchoolDeptResource
import uvicorn

app = FastAPI()

app.include_router(CoilBase().get_router())
app.include_router(CompiledDataResource().get_router())
app.include_router(FacultyRecipientResource().get_router())
app.include_router(GradStudentRecipientResource().get_router())

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)