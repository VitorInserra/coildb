from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://coildb-frontend-dept-coildb.apps.cloudapps.unc.edu", "http://coildb-frontend-dept-coildb.apps.cloudapps.unc.edu:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
