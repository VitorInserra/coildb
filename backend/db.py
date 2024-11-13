from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from dotenv import load_dotenv
import os

load_dotenv(os.getcwd() + '/.env')

DB_USER = os.getenv("DEV_DB_USERNAME")
DB_PASSWORD = os.getenv("DEV_DB_PASSWORD")
DB_HOST = os.getenv("DEV_DB_HOST")
DB_PORT = os.getenv("DEV_DB_PORT")
DB_NAME = os.getenv("DEV_DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DATABASE_URL)

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()