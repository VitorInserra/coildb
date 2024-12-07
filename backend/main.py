from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from api import app

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["POST", "PUT", "OPTIONS", "GET", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
