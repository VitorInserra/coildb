# backend/api.py
from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from resources.coil_base import CoilBase
from resources.compiled_quantitative_data import CompiledDataResource
from resources.faculty_recipient import FacultyRecipientResource
from resources.gradstudent_recipient import GradStudentRecipientResource
from resources.school_dept import SchoolDeptResource
from resources.key_stats import KeyStatisticsResource
import base64
from dotenv import load_dotenv
import os

load_dotenv(os.getcwd() + "/.env")

app = FastAPI()

USERNAME = os.getenv("AUTH_USER", "admin")
PASSWORD = os.getenv("AUTH_PASS", "secret")



app.include_router(CoilBase().get_router())
app.include_router(CompiledDataResource().get_router())
app.include_router(FacultyRecipientResource().get_router())
app.include_router(GradStudentRecipientResource().get_router())
app.include_router(SchoolDeptResource().get_router())
app.include_router(KeyStatisticsResource().get_router())
