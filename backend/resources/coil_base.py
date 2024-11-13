from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from db import get_db

# from models.coil_base import CoilBase

class CoilBase:
    def __init__(self):
        self.router = APIRouter()

    def get_router(self):
        @self.router.get("/ping")
        async def ping(db: Session = Depends(get_db)):
            query = text("SELECT * FROM test_table")

            # Execute the query
            result = db.execute(query)
            
            # Fetch all rows and convert to a list of dictionaries
            rows = [dict(row) for row in result.mappings()]

            print(rows)  # For debugging purposes

            # Return the rows in a structured format
            return {"status": "pong", "data": rows}

        return self.router