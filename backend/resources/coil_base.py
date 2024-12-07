from fastapi import APIRouter, Depends, Response, Request, middleware
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db
from dependencies import get_current_username


class CoilBase:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):

        @self.router.post("/ping")
        async def ping(username: str = Depends(get_current_username)):
            return {"message": "ok"}

        @self.router.options("/")
        async def options_root():
            allowed_methods = ["GET", "OPTIONS"]
            headers = {"Allow": ", ".join(allowed_methods)}
            return JSONResponse(content=None, headers=headers)

        return self.router
