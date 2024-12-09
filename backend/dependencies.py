from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.middleware.cors import CORSMiddleware
import os
import base64
from dotenv import load_dotenv
import secrets


load_dotenv(os.getcwd() + "/.env")

USERNAME = os.getenv("AUTH_USER", "admin")
PASSWORD = os.getenv("AUTH_PASS", "secret")

security = HTTPBasic()


def get_current_username(
    credentials: HTTPBasicCredentials = Depends(security), request: Request = None,
):
    print(credentials)
    if request and request.method == "OPTIONS":
        return
    correct_username = secrets.compare_digest(credentials.username, USERNAME)
    correct_password = secrets.compare_digest(credentials.password, PASSWORD)
    if not (correct_username and correct_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username