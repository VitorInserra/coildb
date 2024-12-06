from fastapi import APIRouter, Depends, Response, Request, middleware
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db

class CoilBase:
    def __init__(self):
        self.router = APIRouter()



    def get_router(self):

        @self.router.get("/ping")
        async def ping(db: Session = Depends(get_db)):
            query = text("SELECT * FROM test_table")
            result = db.execute(query)
            
            rows = [dict(row) for row in result.mappings()]

            print(rows)

            return {"status": "pong", "data": rows}

        return self.router