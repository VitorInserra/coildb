import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from main import app

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

def clear_test_data(db, last_name="Doe"):
    """Helper to clean up specific test data from the gradstudent_recipient table."""
    db.execute(text("DELETE FROM gradstudent_recipient WHERE last_name = :last_name"), {"last_name": last_name})
    db.commit()

def test_create_gradstudent_recipient(override_db, client):
    student_data = {
        "first_name": "John",
        "last_name": "Doe",
        "semester_taught": "Fall",
        "year_taught": 2024,
        "faculty_supervisor": "Dr. Smith",
        "school": "Arts and Sciences",
        "department": "Computer Science",
        "course": "CS101",
        "number": "101",
        "unc_course_name": "Introduction to Computer Science",
        "partner_institution": "Partner University",
        "award": 1500,
    }

    response = client.post("/gradstudent-recipient/post-recipient/", json=student_data)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"

    #Verify data in the database
    db = override_db
    db_recipient = db.execute(
        text("SELECT * FROM gradstudent_recipient WHERE last_name = :last_name"),
        {"last_name": "Doe"}
    ).fetchone()
    assert db_recipient is not None
    assert db_recipient.first_name == "John"

    # Cleanup
    clear_test_data(db)

def test_get_gradstudent_table(override_db, client):
    db = override_db
    db.execute(
        text("INSERT INTO gradstudent_recipient (first_name, last_name, semester_taught, year_taught, faculty_supervisor) VALUES (:first_name, :last_name, :semester_taught, :year_taught, :faculty_supervisor)"),
        {
            "first_name": "John",
            "last_name": "Doe",
            "semester_taught": "Fall",
            "year_taught": 2024,
            "faculty_supervisor": "Dr. Smith",
        }
    )
    db.commit()

    # Test API retrieval
    response = client.get("/gradstudent-recipient/get-recipient")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(recipient["last_name"] == "Doe" for recipient in data)

    # Cleanup
    clear_test_data(db)

def test_get_gradstudent_recipient_by_column(override_db, client):
    db = override_db
    db.execute(
        text("INSERT INTO gradstudent_recipient (first_name, last_name, semester_taught, year_taught) VALUES (:first_name, :last_name, :semester_taught, :year_taught)"),
        {"first_name": "John", "last_name": "Doe", "semester_taught": "Fall", "year_taught": 2024}
    )
    db.commit()

    # Test API retrieval by last_name
    response = client.get("/gradstudent-recipient/get-recipient/last_name/Doe/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Doe"

    # Cleanup
    clear_test_data(db)

def test_delete_gradstudent_recipient(override_db, client):
    db = override_db
    db.execute(
        text("INSERT INTO gradstudent_recipient (first_name, last_name, semester_taught) VALUES (:first_name, :last_name, :semester_taught)"),
        {"first_name": "John", "last_name": "Doe", "semester_taught": "Fall"}
    )
    db.commit()

    #Delete
    response = client.delete("/gradstudent-recipient/delete-recipient/Doe/John")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"

    #Verify deletion in the database
    db_recipient = db.execute(
        text("SELECT * FROM gradstudent_recipient WHERE last_name = :last_name"),
        {"last_name": "Doe"}
    ).fetchone()
    assert db_recipient is None

def test_delete_nonexistent_gradstudent_recipient(client):
    # Attempt to delete a nonexistent record
    response = client.delete("/gradstudent-recipient/delete-recipient/Nonexistent/Name")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "GradStudentRecipient not found"