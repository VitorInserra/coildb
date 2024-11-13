from fastapi import FastAPI, Depends
from resources.coil_base import CoilBase
import uvicorn
from db import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

app = FastAPI()


@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    query = text("SELECT * FROM test_table")

    # Execute the query
    result = db.execute(query)
    
    # Fetch all rows and convert to a list of dictionaries
    rows = [dict(row) for row in result.mappings()]

    print(rows)  # For debugging purposes

    # Return the rows in a structured format
    return {"status": "pong", "data": rows}

coil_base = CoilBase()
app.include_router(coil_base.get_router())

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)