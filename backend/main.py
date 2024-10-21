from fastapi import FastAPI, Depends
from typing import List
from datetime import datetime
import uvicorn

app = FastAPI()


@app.get("/ping")
def ping():
    return "pong"


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)