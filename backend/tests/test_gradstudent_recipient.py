import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.gradstudent_recipient import GradStudentRecipient
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

url_base = '/gradstudent-recipient'


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

@pytest.fixture(autouse=True)
def override_dependency():
    app.dependency_overrides[TestSessionLocal] = lambda: TestSessionLocal()

def test_get_gradstudents(override_db, client):
    student_1 = GradStudentRecipient(
        first_name="John",
        last_name="Doe",
        semester_taught="Fall",
        year_taught=2024,
        faculty_supervisor="Dr. Smith",
        school="Arts and Sciences",
        department="Computer Science",
        course="CS101",
        number="101",
        unc_course_name="Introduction to Computer Science",
        partner_institution="Partner University",
        award=1500,
    )
    student_2 = GradStudentRecipient(
        first_name="Jane",
        last_name="Smith",
        semester_taught="Spring",
        year_taught=2023,
        faculty_supervisor="Dr. Johnson",
        school="Engineering",
        department="Electrical Engineering",
        course="EE201",
        number="201",
        unc_course_name="Circuits and Systems",
        partner_institution="Engineering College",
        award=2000,
    )

    override_db.add_all([student_1, student_2])
    override_db.commit()

    response = client.get(url_base + "/gradstudent-recipient/")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Doe"
    assert data[0]["semester_taught"] == "Fall"
    assert data[0]["year_taught"] == 2024
    assert data[0]["department"] == "Computer Science"
    assert data[0]["course"] == "CS101"
    assert data[0]["number"] == "101"
    assert data[0]["unc_course_name"] == "Introduction to Computer Science"
    assert data[0]["partner_institution"] == "Partner University"
    assert data[0]["award"] == 1500
    assert data[1]["first_name"] == "Jane"
    assert data[1]["last_name"] == "Smith"
    assert data[1]["semester_taught"] == "Spring"
    assert data[1]["year_taught"] == 2023
    assert data[1]["department"] == "Electrical Engineering"
    assert data[1]["course"] == "EE201"
    assert data[1]["number"] == "201"
    assert data[1]["unc_course_name"] == "Circuits and Systems"
    assert data[1]["partner_institution"] == "Engineering College"
    assert data[1]["award"] == 2000


def test_create_gradstudent(override_db, client):
    new_student = {
        "first_name": "Alice",
        "last_name": "Wonderland",
        "semester_taught": "Winter",
        "year_taught": 2022,
        "faculty_supervisor": "Dr. Brown",
        "school": "Medicine",
    }

    response = client.post(url_base + "/gradstudent-recipient/", json=new_student)

    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Alice"
    assert data["last_name"] == "Wonderland"
    assert data["semester_taught"] == "Winter"
    assert data["year_taught"] == 2022


    student_in_db = (
        override_db.query(GradStudentRecipient)
        .filter_by(first_name="Alice", last_name="Wonderland")
        .first()
    )
    assert student_in_db is not None

def test_delete_gradstudent_recipient(override_db, client):
    student = GradStudentRecipient(
        first_name="Eve",
        last_name="Adams",
        semester_taught="Summer",
        year_taught=2023,
        faculty_supervisor="Dr. Clark",
        school="Business",
    )
    override_db.add(student)
    override_db.commit()

    response = client.delete(url_base + "/delete-recipient/Adams/Eve")

    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "Eve"
    assert data["last_name"] == "Adams"


    remaining_students = override_db.query(GradStudentRecipient).all()
    assert all(
        s.first_name != "Eve" or s.last_name != "Adams" for s in remaining_students
    )

def test_delete_nonexistent_gradstudent_recipient(client):
    response = client.delete("/delete-recipient/Nonexistent/Name")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
