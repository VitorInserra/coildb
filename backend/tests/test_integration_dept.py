import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from main import app
from models.schemas.school_dept import DepartmentModel

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
school_data = DepartmentModel(
    department="test_dept",
    course="test_course"
)
def helper_delete_dept(client, dept: str, course: str):
    response = client.delete(
        f"/school-dept/delete-dept/{dept}/{course}/"
    )

def test_create_dept(override_db, client):
    helper_delete_dept(client, "test_dept", "test_course")
    response = client.post("/school-dept/department/", json=school_data.dict())
    data = response.json()
    assert data["department"] == "test_dept"
    db_school = override_db.execute(
        text(""" SELECT * FROM departments WHERE "department" = :dept """),
        {"dept": "test_dept"}
    ).fetchone()
    assert db_school is not None
    assert db_school[1] == "test_course"
    helper_delete_dept(client, "test_dept", "test_course")

def test_get_dept_table(override_db, client):
     # Cleanup
    helper_delete_dept(client, "test_dept", "test_course")
    response = client.post("/school-dept/department/", json=school_data.dict())
    # Test API retrieval
    response = client.get("/school-dept/departments_table")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(recipient["department"] == "test_dept" for recipient in data)
    db_school = override_db.execute(
        text(""" SELECT * FROM departments WHERE "department" = :dept """),
        {"dept": "test_dept"}
    ).fetchone()
    assert db_school[1] == "test_course"
    # Cleanup
    helper_delete_dept(client, "test_dept", "test_course")


def test_get_nonexistent_dept(client):
    # Test API retrieval for a nonexistent last_name
    response = client.get("/school-dept/get-department/department/Nonexistent/")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Department not found"

def test_delete_dept(override_db, client):
    helper_delete_dept(client, "test_dept", "test_course")
    response = client.post("/school-dept/department/", json=school_data.dict())
    #Delete 
    dept = "test_dept"
    course = "test_course"
    response = client.delete(f"/school-dept/delete-dept/{dept}/{course}/")
    assert response.status_code == 200

    #Verify deletion in the database
    db_recipient = override_db.execute(text("SELECT * FROM departments WHERE 'department' = :dept"), {"dept": "test_dept"}).fetchone()
    assert db_recipient is None
    helper_delete_dept(client, "test_dept", "test_course")


def test_delete_nonexistent_department(client):
    #Attempt to delete a nonexistent record
    response = client.delete("/school-dept/delete-dept/department/nonexistent")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "Department not found"
