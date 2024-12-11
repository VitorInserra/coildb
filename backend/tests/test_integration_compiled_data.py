import pytest
from fastapi.testclient import TestClient
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from db import engine
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

def clear_test_data(db, semester=None):
    """Helper to clean up specific test data from the compiled_data table."""
    if semester:
        db.execute(
            text("DELETE FROM compiled_data WHERE semester = :semester"),
            {"semester": semester},
        )
    else:
        db.execute(text("DELETE FROM compiled_data"))
    db.commit()

def test_add_hard_coded(override_db, client):
    db = override_db
    clear_test_data(db, semester="Fall 2024")

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

    #Verify data in the database
    db_data = db.execute(
        text("SELECT * FROM compiled_data WHERE semester = :semester"),
        {"semester": "Fall 2024"},
    ).fetchone()
    assert db_data is not None
    assert db_data.semester == "Fall 2024"
    assert db_data.undergrad_fdoc == 100

    # Cleanup
    clear_test_data(db, semester="Fall 2024")

def test_add_duplicate_hard_coded(override_db, client):
    db = override_db
    clear_test_data(db, semester="Fall 2024")

    db.execute(
        text(
            "INSERT INTO compiled_data (semester, undergrad_fdoc) VALUES (:semester, :undergrad_fdoc)"
        ),
        {"semester": "Fall 2024", "undergrad_fdoc": 100},
    )
    db.commit()

    # Test adding duplicate data
    response = client.post(
        "/compiled-data/add-hard-coded",
        params={"semester": "Fall 2024"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Fall 2024' already exists. No data added."}

    # Cleanup
    clear_test_data(db, semester="Fall 2024")

def test_get_compiled_data(override_db, client):
    db = override_db
    clear_test_data(db)

    db.execute(
        text(
            "INSERT INTO compiled_data (semester, undergrad_fdoc) VALUES (:semester, :undergrad_fdoc)"
        ),
        {"semester": "Fall 2024", "undergrad_fdoc": 100},
    )
    db.commit()

    # Test retrieval
    response = client.get(
        "/compiled-data/get-data/",
        params={"semesters": ["Fall 2024"]},
    )
    assert response.status_code == 200
    data = response.json()
    assert "Fall 2024" in data

    # Cleanup
    clear_test_data(db)

def test_update_hard_coded(override_db, client):
    db = override_db
    clear_test_data(db, semester="Fall 2024")

    db.execute(
        text(
            "INSERT INTO compiled_data (semester, undergrad_fdoc) VALUES (:semester, :undergrad_fdoc)"
        ),
        {"semester": "Fall 2024", "undergrad_fdoc": 100},
    )
    db.commit()

    # Test update
    response = client.put(
        "/compiled-data/update-hard-coded",
        params={
            "semester": "Fall 2024",
            "undergrad_fdoc": 120,
        },
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Fall 2024' updated successfully."}

    # Verify database update
    db_data = db.execute(
        text("SELECT undergrad_fdoc FROM compiled_data WHERE semester = :semester"),
        {"semester": "Fall 2024"},
    ).fetchone()
    assert db_data.undergrad_fdoc == 120

    # Cleanup
    clear_test_data(db, semester="Fall 2024")

def test_update_nonexistent_hard_coded(override_db, client):
    db = override_db
    clear_test_data(db)

    # Test update for nonexistent semester
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
    db = override_db
    clear_test_data(db, semester="Fall 2024")

    db.execute(
        text(
            "INSERT INTO compiled_data (semester, undergrad_fdoc) VALUES (:semester, :undergrad_fdoc)"
        ),
        {"semester": "Fall 2024", "undergrad_fdoc": 100},
    )
    db.commit()

    #deletion
    response = client.delete(
        "/compiled-data/delete-by-semester",
        params={"semester": "Fall 2024"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "Semester 'Fall 2024' deleted successfully."}

    # Verify deletion
    db_data = db.execute(
        text("SELECT * FROM compiled_data WHERE semester = :semester"),
        {"semester": "Fall 2024"},
    ).fetchone()
    assert db_data is None

    # Cleanup
    clear_test_data(db)

def test_delete_nonexistent_semester(override_db, client):
    db = override_db
    clear_test_data(db)

    # Test deletion for nonexistent semester
    response = client.delete(
        "/compiled-data/delete-by-semester",
        params={"semester": "Spring 2025"},
    )
    assert response.status_code == 200
    assert response.json() == {"message": "No row found for semester 'Spring 2025'. No deletion performed."}