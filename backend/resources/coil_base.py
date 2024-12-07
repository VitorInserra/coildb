from fastapi import APIRouter, Depends, Response, Request, middleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db
from dependencies import get_current_username


class CoilBase:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):

        @self.router.get("/ping")
        async def ping(
            username: str = Depends(get_current_username)
        ):
            return {"message": "ok"}

        return self.router
