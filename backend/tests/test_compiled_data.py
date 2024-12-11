import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from db import Base, engine
from main import app
from resources.compiled_quantitative_data import CompiledDataResource  

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



def test_add_hard_coded(override_db, client):
    response = client.post(
        "/compiled-data/add-hard-coded",
        params={
            "semester": "Fall 2024",
            "undergrad_fdoc": 100,
            "grad_fdoc": 50,
            "undergrad_ldoc": 30,
            "grad_ldoc": 20,
            "eligible_ee_credit": 10,
            "received_ee_credit": 5,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Data added successfully"}

def test_add_duplicate_hard_coded(override_db, client):
    response = client.post(
        "/compiled-data/add-hard-coded",
        params={"semester": "Fall 2024"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Fall 2024' already exists. No data added."}

def test_get_compiled_quantity_data(override_db, client):
    response = client.get(
        "/compiled-data/get-quantity-data/",
        params={"semesters": ["Fall 2023"] }
    )
    assert response.status_code == 200
    data = response.json()
    assert "coil_courses_offered" in data["Fall 2023"]

def test_update_hard_coded(override_db, client):
    response = client.put(
        "/compiled-data/update-hard-coded",
        params={
            "semester": "Fall 2024",
            "undergrad_fdoc": 120,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Fall 2024' updated successfully."}

def test_update_nonexistent_hard_coded(override_db, client):
    response = client.put(
        "/compiled-data/update-hard-coded",
        params={
            "semester": "Spring 2025",
            "undergrad_fdoc": 120,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Spring 2025' not found. No updates made."}

def test_delete_by_semester(override_db, client):
    response = client.delete(
        "/compiled-data/delete-by-semester",
        params={"semester": "Fall 2024"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Fall 2024' deleted successfully."}

def test_delete_nonexistent_semester(override_db, client):
    response = client.delete(
        "/compiled-data/delete-by-semester",
        params={"semester": "Spring 2025"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "No row found for semester 'Spring 2025'. No deletion performed."}
