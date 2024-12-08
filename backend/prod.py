from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api import app, create_auth_middleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://coildb-frontend-dept-coildb.apps.cloudapps.unc.edu"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["Authorization", "Content-Type"],
)

create_auth_middleware(app)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
