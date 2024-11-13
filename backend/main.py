from fastapi import FastAPI
from resources.coil_base import CoilBase
from resources.compiled_quantitative_data import CompiledDataResource
# from resources.faculty_recipient import FacultyRecipient
# from resources.gradstudent_recipient import GradStudentRecipient
# from resources.school_dept import SchoolDeptResource
import uvicorn

app = FastAPI()

app.include_router(CoilBase().get_router())
app.include_router(CompiledDataResource().get_router())

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)