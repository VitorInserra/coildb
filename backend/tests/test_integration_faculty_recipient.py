import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from models.schemas.faculty_recipient import FacultyRecipientModel
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

faculty_data = FacultyRecipientModel(
        first_name="jon",
        last_name="jones",
        email="jonjones@example.com",
        semester_taught="test 2024",
        course_title="test to Programming",
        school="test of Engineering",
        department="test Science",
        course_name="test",
        course_number="test",
        sections="A",
        total_sections_taught=1,
        co_taught_semester=None,
        co_taught_year=None,
        repeat_course_semester=None,
        repeat_course_year=None,
        joint_course=None,
        quarter=None,
        estimated_unc_students=30,
        estimated_partner_students=25,
        unc_students_fdoc_count=28,
        unc_students_ldoc_count=26,
        partner_institution1="Example University",
        partner_country1="USA",
        partner_faculty1="Dr. Smith",
        partner_institution2="Another University",
        partner_country2="Canada",
        partner_faculty2="Dr. Brown",
        credit="3 credits",
        graduate_student="Jane Graduate",
        faculty_amount_rewarded=5000,
        graduate_award_student_amount=2000,
        repeat_award=None,
        repeat_award_criteria=None,
        coil_champions="Yes",
        notes="First semester teaching",
        partner_region="North America",
        cancelled=False
    )
def helper_delete_faculty_recipient(client, first_name: str, last_name: str):
    response = client.delete(
        f"/faculty-recipient/delete-recipient/first-last-name/{first_name}/{last_name}"
    )
    assert response.status_code in [200, 404], "Delete operation failed or record not found"

def test_create_faculty_recipient(override_db, client):
     # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")
    response = client.post("/faculty-recipient/post-recipient/", json=faculty_data.dict())
    data = response.json()
    assert data["first_name"] == "jon"
    assert data["last_name"] == "jones"

    #Verify data in the database
    db_recipient = override_db.execute(
        text(""" SELECT * FROM faculty WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipient is not None
    assert db_recipient[0] == "jones"
    assert db_recipient[1] == "jon"

    # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")

def test_get_faculty_table(override_db, client):
     # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")
    response = client.post("/faculty-recipient/post-recipient/", json=faculty_data.dict())
    # Test API retrieval
    response = client.get("/faculty-recipient/get-recipient")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(recipient["last_name"] == "jones" for recipient in data)
    # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")


def test_get_faculty_recipient_by_column(override_db, client):
     # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")
    client.post("/faculty-recipient/post-recipient/", json=faculty_data.dict())
    # Test API retrieval
    response = client.get("/faculty-recipient/get-recipient/last_name/jones/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["first_name"] == "jon"
    assert data[0]["last_name"] == "jones"
    db_recipient = override_db.execute(
        text(""" SELECT * FROM faculty WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipient[1] == "jon"

    # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")

def test_get_nonexistent_faculty_recipient(override_db, client):
    # Test API retrieval for a nonexistent last_name
    response = client.get("/faculty-recipient/get-recipient/last_name/Nonexistent/")
    assert response.status_code == 200
    data = response.json()
    assert "first_name" in data
    assert data["first_name"] == None
    db_recipient = override_db.execute(
        text(""" SELECT * FROM faculty WHERE "Last Name" = :last_name """),
        {"last_name": "Nonexistent"}
    ).fetchone()
    assert db_recipient is None

def test_delete_faculty_recipient(override_db, client):
      # Cleanup
    helper_delete_faculty_recipient(client, "jon", "jones")
    client.post("/faculty-recipient/post-recipient/", json=faculty_data.dict())
    db_recipient = override_db.execute(
        text(""" SELECT * FROM faculty WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipient is not None

    #Delete 
    first = "jon"
    last = "jones"
    response = client.delete(f"/faculty-recipient/delete-recipient/first-last-name/{first}/{last}")
    assert response.status_code == 200

    #Verify deletion in the database
    db_recipientt = override_db.execute(
        text(""" SELECT * FROM faculty WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipientt is None

def test_delete_nonexistent_faculty_recipient(override_db, client):
    #Attempt to delete a nonexistent record
    response = client.delete("/faculty-recipient/delete-recipient/first-last-name/Nonexistent/Nonexistent")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "FacultyRecipient not found"
    db_recipient = override_db.execute(
        text(""" SELECT * FROM faculty WHERE "Last Name" = :last_name """),
        {"last_name": "Nonexistent"}
    ).fetchone()
    assert db_recipient is None