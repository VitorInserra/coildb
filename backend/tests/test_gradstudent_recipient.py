import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from models.gradstudent_recipient import GradStudentRecipient
from models.schemas.gradstudent_recipient import GradStudentRecipientModel
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

new_student = GradStudentRecipientModel(
        first_name= "Alice",
        last_name= "Wonderland",
        semester_taught= "Winter",
        year_taught= 2022,
        faculty_supervisor= "Dr. Brown",
        school= "Medicine",
        course="test",
        department = "test",
        number = "0",
        unc_course_name = "test",
        partner_institution ="test",
        award = 0,
        email = "test",
        pid = 0
)

def test_get_gradstudents(override_db, client):
    response = client.delete("/gradstudent-recipient/delete-recipient/first-last-name/Alice/Wonderland")
    #cleanup
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=new_student.dict())
    response = client.get("/gradstudent-recipient/gradstudent-recipient/")

    assert response.status_code == 200
    data = response.json()
    assert any(recipient["last_name"] == "Wonderland" for recipient in data)
    assert any(recipient["first_name"] == "Alice" for recipient in data)
    response = client.delete("/faculty-recipient/delete-recipient/first-last-name/Alice/Wonderland")
    #cleanup




def test_create_gradstudent(override_db, client):
    response = client.delete("/gradstudent-recipient/delete-recipient/first-last-name/Alice/Wonderland")
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=new_student.dict())
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
    #Cleanup
    response = client.delete("/gradstudent-recipient/delete-recipient/first-last-name/Alice/Wonderland")
    #Add test
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=new_student.dict())
    response = client.get("/gradstudent-recipient/get-recipient/last_name/Wonderland")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["first_name"] == "Alice"
    assert data[0]["last_name"] == "Wonderland"

    #Delete test
    response = client.delete("/gradstudent-recipient/delete-recipient/first-last-name/Alice/Wonderland")
    response = client.get("/gradstudent-recipient/get-recipient/last_name/Wonderland")
    data = response.json()
    assert data["first_name"] == None
    assert data["last_name"] == None

def test_delete_nonexistent_gradstudent_recipient(client):
    response = client.delete("/delete-recipient/Nonexistent/Name")

    assert response.status_code == 404
    assert response.json() == {"detail": "Not Found"}
