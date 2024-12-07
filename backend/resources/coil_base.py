from fastapi import APIRouter, Depends, Response, Request, middleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import os
from dotenv import load_dotenv
from dependencies import get_current_username

load_dotenv(os.getcwd() + "/.env")

security = HTTPBasic()
USERNAME = os.getenv("AUTH_USER", "admin")
PASSWORD = os.getenv("AUTH_PASS", "secret")


class CoilBase:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):

        @self.router.post("/ping")
        def ping(username: str = Depends(get_current_username)):
            return {"message": "ok"}

        return self.router
