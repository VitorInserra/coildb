import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from db import get_db, Base
from main import app
import os
from dotenv import load_dotenv


load_dotenv(os.getcwd() + '/.env')

DB_USER = os.getenv("DEV_DB_USERNAME")
DB_PASSWORD = os.getenv("DEV_DB_PASSWORD")
DB_HOST = os.getenv("DEV_DB_HOST")
DB_PORT = os.getenv("DEV_DB_PORT")
DB_NAME = os.getenv("DEV_DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DATABASE_URL)

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def test_db():
    """
    Creates a new database session for a test and tears down after the test.
    """

    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db 
    finally:
        db.close()
        Base.metadata.drop_all(bind=engine) 

@pytest.fixture(scope="function")
def client(test_db):
    """
    Overrides FastAPI's dependency to use the test database session.
    Returns a TestClient instance for making requests.
    """
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()


    app.dependency_overrides[get_db] = override_get_db


    with TestClient(app) as test_client:
        yield test_client