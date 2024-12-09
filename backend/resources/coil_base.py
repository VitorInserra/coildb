from fastapi import APIRouter, Depends, Response, Request, middleware
from sqlalchemy import text
from fastapi import Depends
import os
from dependencies import get_current_username


class CoilBase:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):

        @self.router.get("/ping", dependencies=[Depends(get_current_username)])
        def ping():
            return {"message": "ok"}


        return self.router
