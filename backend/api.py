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
import base64
from dotenv import load_dotenv
import os

load_dotenv(os.getcwd() + "/.env")

app = FastAPI()

USERNAME = os.getenv("AUTH_USER", "admin")
PASSWORD = os.getenv("AUTH_PASS", "secret")

def create_auth_middleware(app: FastAPI):
    @app.middleware("http")
    async def basic_auth_middleware(request: Request, call_next):
        if request.method == "OPTIONS":
            return await call_next(request)

        if request.method not in ["POST", "PUT", "DELETE", "GET"]:
            return await call_next(request)

        auth = request.headers.get("Authorization")

        if not auth:
            return Response(
                status_code=401,
                headers={"WWW-Authenticate": 'Basic realm="Login Required"'},
            )

        if not auth.startswith("Basic "):
            return Response(
                status_code=401,
                headers={"WWW-Authenticate": 'Basic realm="Login Required"'},
            )

        encoded_credentials = auth[len("Basic ") :].strip()
        try:
            decoded = base64.b64decode(encoded_credentials).decode("utf-8")
            username, password = decoded.split(":", 1)
        except Exception:
            return Response(
                status_code=401,
                headers={"WWW-Authenticate": 'Basic realm="Login Required"'},
            )

        if username != USERNAME or password != PASSWORD:
            return Response(
                status_code=401,
                headers={"WWW-Authenticate": 'Basic realm="Login Required"'},
            )

        return await call_next(request)

app.include_router(CoilBase().get_router())
app.include_router(CompiledDataResource().get_router())
app.include_router(FacultyRecipientResource().get_router())
app.include_router(GradStudentRecipientResource().get_router())
app.include_router(SchoolDeptResource().get_router())
