from fastapi import APIRouter
# from models.coil_base import CoilBase

class CoilBase:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):
        @self.router.get("/ping")
        async def ping():
            return "pong"

        return self.router