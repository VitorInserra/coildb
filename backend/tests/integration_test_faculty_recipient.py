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
    """Helper to clean up specific test data from the faculty_recipient table."""
    db.execute(text("DELETE FROM faculty_recipient WHERE last_name = :last_name"), {"last_name": last_name})
    db.commit()

def test_create_faculty_recipient(override_db, client):
    faculty_data = {
        "first_name": "John",
        "last_name": "Doe",
        "email": "jdoe@example.com",
        "semester_taught": "Fall 2024",
        "course_title": "Introduction to Programming",
        "department": "Computer Science",
        "school": "School of Engineering",
        # Add all required fields as needed...
        "cancelled": False,
    }
    response = client.post("/faculty-recipient/post-recipient/", json=faculty_data)
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"

    #Verify data in the database
    db = override_db
    db_recipient = db.execute(text("SELECT * FROM faculty_recipient WHERE last_name = :last_name"), {"last_name": "Doe"}).fetchone()
    assert db_recipient is not None
    assert db_recipient.first_name == "John"

    # Cleanup
    clear_test_data(db)

def test_get_faculty_table(override_db, client):
    db = override_db
    db.execute(
        text("INSERT INTO faculty_recipient (first_name, last_name, email, course_title, semester_taught) VALUES (:first_name, :last_name, :email, :course_title, :semester_taught)"),
        {
            "first_name": "John",
            "last_name": "Doe",
            "email": "jdoe@example.com",
            "course_title": "Introduction to Programming",
            "semester_taught": "Fall 2024",
        }
    )
    db.commit()

    # Test API retrieval
    response = client.get("/faculty-recipient/get-recipient")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(recipient["last_name"] == "Doe" for recipient in data)

    # Cleanup
    clear_test_data(db)

def test_get_faculty_recipient_by_column(override_db, client):
    db = override_db
    db.execute(
        text("INSERT INTO faculty_recipient (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"),
        {"first_name": "John", "last_name": "Doe", "email": "jdoe@example.com"}
    )
    db.commit()

    # Test API retrieval by last_name
    response = client.get("/faculty-recipient/get-recipient/last_name/Doe/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Doe"

    # Cleanup
    clear_test_data(db)

def test_get_nonexistent_faculty_recipient(client):
    # Test API retrieval for a nonexistent last_name
    response = client.get("/faculty-recipient/get-recipient/last_name/Nonexistent/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["message"] == "No matching faculty recipient found"

def test_delete_faculty_recipient(override_db, client):
    db = override_db
    db.execute(
        text("INSERT INTO faculty_recipient (first_name, last_name, email) VALUES (:first_name, :last_name, :email)"),
        {"first_name": "John", "last_name": "Doe", "email": "jdoe@example.com"}
    )
    db.commit()

    #Delete 
    response = client.delete("/faculty-recipient/delete-recipient/Doe/John")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"

    #Verify deletion in the database
    db_recipient = db.execute(text("SELECT * FROM faculty_recipient WHERE last_name = :last_name"), {"last_name": "Doe"}).fetchone()
    assert db_recipient is None

def test_delete_nonexistent_faculty_recipient(client):
    #Attempt to delete a nonexistent record
    response = client.delete("/faculty-recipient/delete-recipient/Nonexistent/Name")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "FacultyRecipient not found"