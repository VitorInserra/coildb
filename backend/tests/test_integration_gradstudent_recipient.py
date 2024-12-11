import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from main import app
from models.schemas.gradstudent_recipient import GradStudentRecipientModel

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

grad_data = GradStudentRecipientModel(
    semester_taught="test 2024",
    year_taught=2024,
    last_name="jones",
    first_name="jon",
    faculty_supervisor=None,
    school="test of Engineering",
    department="test Science",
    course="test",
    number="test",
    unc_course_name=None,
    partner_institution="Example University",
    award=5000,
    pid=12345,
    email="jonjones@example.com"
)
def helper_delete_gradstudent_recipient(client, first_name: str, last_name: str):
    response = client.delete(
        f"/gradstudent-recipient/delete-recipient/first-last-name/{first_name}/{last_name}"
    )
    assert response.status_code in [200, 404], "Delete operation failed or record not found"

def test_create_gradstudent_recipient(override_db, client):
    helper_delete_gradstudent_recipient(client, "jon", "jones")
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=grad_data.dict())
    assert response.status_code == 200
    data = response.json()
    assert data["first_name"] == "jon"
    assert data["last_name"] == "jones"

    #Verify data in the database
    db_recipient = override_db.execute(
        text(""" SELECT * FROM grad_student WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipient[2] == "jones"
    assert db_recipient[3] == "jon"
    helper_delete_gradstudent_recipient(client, "jon", "jones")


def test_get_gradstudent_table(override_db, client):
    helper_delete_gradstudent_recipient(client, "jon", "jones")
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=grad_data.dict())
    # Test API retrieval
    response = client.get("/gradstudent-recipient/gradstudent-recipient")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert any(recipient["last_name"] == "jones" for recipient in data)
    helper_delete_gradstudent_recipient(client, "jon", "jones")


def test_get_gradstudent_recipient_by_column(override_db, client):
    helper_delete_gradstudent_recipient(client, "jon", "jones")
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=grad_data.dict())
    # Test API retrieval by last_name
    response = client.get("/gradstudent-recipient/get-recipient/last_name/jones/")
    assert response.status_code == 200
    data = response.json()
    assert data[0]["first_name"] == "jon"
    assert data[0]["last_name"] == "jones"
    db_recipient = override_db.execute(
        text(""" SELECT * FROM grad_student WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipient[3] == "jon"
    helper_delete_gradstudent_recipient(client, "jon", "jones")


def test_delete_gradstudent_recipient(override_db, client):
    helper_delete_gradstudent_recipient(client, "jon", "jones")
    response = client.post("/gradstudent-recipient/gradstudent-recipient/", json=grad_data.dict())

    #Delete
    client.delete("/gradstudent-recipient/delete-recipient/first-last-name/jon/jones")
    assert response.status_code == 200
    data = response.json()

    #Verify deletion in the database
    db_recipient = override_db.execute(
        text(""" SELECT * FROM grad_student WHERE "Last Name" = :last_name """),
        {"last_name": "jones"}
    ).fetchone()
    assert db_recipient is None

def test_delete_nonexistent_gradstudent_recipient(override_db, client):
    # Attempt to delete a nonexistent record
    response = client.delete("/gradstudent-recipient/delete-recipient/first-last-name/nonexist/nonexist")
    assert response.status_code == 404
    data = response.json()
    assert data["detail"] == "GradStudentRecipient not found"
    db_recipient = override_db.execute(
        text(""" SELECT * FROM grad_student WHERE "Last Name" = :last_name """),
        {"last_name": "nonexist"}
    ).fetchone()
    assert db_recipient is None