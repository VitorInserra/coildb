import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from main import app
from models.schemas.school_dept import SchoolCreateModel, SchoolModel

TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def override_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()
school_data = SchoolCreateModel(
    school="test",
    school_count=100,
    repeat_faculty=0,
    unique_faculty=0
)
def helper_delete_school(client, name: str):
    response = client.delete(
        f"/school-dept/delete-school/{name}"
    )

def test_create_school(override_db, client):
    helper_delete_school(client, "test")
    response = client.post("/school-dept/schools/", json=school_data.dict())
    data = response.json()
    assert data["school"] == "test"
    db_school = override_db.execute(
        text(""" SELECT * FROM schools WHERE "school" = :school """),
        {"school": "test"}
    ).fetchone()
    assert db_school is not None
    assert db_school[0] == "test"
    helper_delete_school(client, "test")

def get_school_table(override_db, client):
     # Cleanup
    helper_delete_school(client, "test")
    response = client.post("/school-dept/schools/", json=school_data.dict())
    # Test API retrieval
    response = client.get("/school-dept/schools_table")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(recipient["school"] == "test" for recipient in data)
    db_school = override_db.execute(
        text(""" SELECT * FROM schools WHERE "School" = :school """),
        {"school": "test"}
    ).fetchone()
    assert db_school[0] == "test"
    # Cleanup
    helper_delete_school(client, "test")