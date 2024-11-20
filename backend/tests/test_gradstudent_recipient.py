import pytest
from fastapi.testclient import TestClient
from main import app
from db import SessionLocal
from models.gradstudent_recipient import GradStudentRecipient

client = TestClient(app)


@pytest.fixture
def override_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def test_get_gradstudents(override_db, client):
    student_1 = GradStudentRecipient(
        first_name="John",
        last_name="Doe",
        semester_taught="Fall",
        year_taught=2024,
        faculty_supervisor="Dr. Smith",
        school="Arts and Sciences",
    )
    student_2 = GradStudentRecipient(
        first_name="Jane",
        last_name="Smith",
        semester_taught="Spring",
        year_taught=2023,
        faculty_supervisor="Dr. Johnson",
        school="Engineering",
    )

    override_db.add_all([student_1, student_2])
    override_db.commit()

    response = client.get("/gradstudent-recipient/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Doe"
    assert data[0]["semester_taught"] == "Fall"
    assert data[0]["year_taught"] == 2024
    assert data[1]["first_name"] == "Jane"
    assert data[1]["last_name"] == "Smith"
    assert data[1]["semester_taught"] == "Spring"
    assert data[1]["year_taught"] == 2023


def test_create_gradstudent(override_db):
    new_student = {
        "first_name": "Alice",
        "last_name": "Wonderland",
        "semester_taught": "Winter",
        "year_taught": 2022,
        "faculty_supervisor": "Dr. Brown",
        "school": "Medicine",
    }

    response = client.post("/gradstudent-recipient/", json=new_student)

    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Alice"
    assert data["last_name"] == "Wonderland"
    assert data["semester_taught"] == "Winter"
    assert data["year_taught"] == 2022


def test_delete_gradstudent_recipient(override_db):
    student = GradStudentRecipient(
        first_name="Eve",
        last_name="Adams",
        semester_taught="Summer",
        year_taught=2023,
        faculty_supervisor="Dr. Clark",
        school="Business",
        department="Engineering",
        course="CS101",
        number="1",
        unc_course_name="Intro to Computer Science",
        partner_institution="Fake Uni",
        award=1000,
    )
    override_db.add(student)
    override_db.commit()

    response = client.delete("/delete-recipient/Adams/Eve")

    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Eve"
    assert data["last_name"] == "Adams"

    response = client.get("/gradstudent-recipient/")
    remaining_students = response.json()
    assert all(
        s["first_name"] != "Eve" or s["last_name"] != "Adams"
        for s in remaining_students
    )

def test_delete_nonexistent_gradstudent_recipient(override_db):
    response = client.delete("/delete-recipient/Nonexistent/Name")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
