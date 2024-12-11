import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.faculty_recipient import FacultyRecipient
from models.schemas.faculty_recipient import FacultyRecipientModel
from resources.faculty_recipient import FacultyRecipientResource
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
        first_name= "John",
        last_name= "Doe",
        email= "jdoe@example.com",
        semester_taught= "Fall 2024",
        course_title= "Introduction to Programming",
        department= "Computer Science",
        school= "School of Engineering",
        course_name= "CS101",
        course_number= "101",
        sections= "2",
        total_sections_taught= 2,
        co_taught_semester= "Spring",
        co_taught_year= 2023,
        repeat_course_semester= "Fall",
        repeat_course_year= 2023,
        joint_course= "Yes",
        quarter= "Q1",
        estimated_unc_students= 50,
        estimated_partner_students= 30,
        unc_students_fdoc_count= 48,
        unc_students_ldoc_count= 46,
        partner_institution1= "Partner University",
        partner_country1= "USA",
        partner_faculty1= "Dr. Smith",
        partner_institution2= None,
        partner_country2= None,
        partner_faculty2= None,
        credit= "EE",
        graduate_student= "Yes",
        faculty_amount_rewarded= 5000,
        graduate_award_student_amount= 1000,
        repeat_award= "Yes",
        repeat_award_criteria= "High Impact",
        coil_champions= "Yes",
        notes= "Test data for faculty recipient",
        partner_region= "North America",
        cancelled= False,
)

def test_create_faculty_recipient(client):
    #cleanup
    response = client.delete("/faculty-recipient/delete-recipient/first-last-name/John/Doe")
    #start test
    response = client.post("/faculty-recipient/post-recipient/", json=faculty_data.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"
    assert data["email"] == "jdoe@example.com"
    assert data["semester_taught"] == "Fall 2024"
    assert data["course_title"] == "Introduction to Programming"
    assert data["department"] == "Computer Science"
    assert data["school"] == "School of Engineering"


def test_get_faculty_table(client):
    response = client.get("/faculty-recipient/get-recipient")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["first_name"] == "Shorna"
    assert data[0]["last_name"] == "Allred"
    assert any(recipient["last_name"] == "Doe" for recipient in data)


def test_get_faculty_recipient_by_column(client):
    response = client.get("/faculty-recipient/get-recipient/last_name/Doe/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) >= 1
    assert data[0]["first_name"] == "John"
    assert data[0]["last_name"] == "Doe"


def test_get_nonexistent_faculty_recipient(client):
    column = "last_name"
    input = "nonexistenttestname"
    response = client.get(f"/faculty-recipient/get-recipient/{column}/{input}/")
    assert response.status_code == 200
    data = response.json()
    assert "first_name" in data
    assert "last_name" in data
    assert data["first_name"] == None
    assert data["last_name"] == None


def test_delete_faculty_recipient(client):
    response = client.delete("/faculty-recipient/delete-recipient/first-last-name/John/Doe")
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "John"
    assert data["last_name"] == "Doe"

    response = client.get("/faculty-recipient/get-recipient/last_name/Doe/")
    assert response.status_code == 200
    data = response.json()
    assert "first_name" in data
    assert "last_name" in data
    assert data["first_name"] == None
    assert data["last_name"] == None


def test_delete_nonexistent_faculty_recipient(client):
    response = client.delete("/faculty-recipient/delete-recipient/first-last-name/nonexistent/nonexistent")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "FacultyRecipient not found"
