from sqlalchemy import func
from sqlalchemy.orm import Session
from models.school_dept import School
from models.faculty_recipient import FacultyRecipient

def update_faculty_counts(db: Session):
    result = (
    db.query(
        School.id,
        func.count(FacultyRecipient.school).label("repeat_faculty"),  # Count how many times FacultyRecipient.school matches School.school
        (School.school_count - func.count(FacultyRecipient.school)).label("unique_faculty"),  # Calculate unique faculty count
    )
    .outerjoin(FacultyRecipient, FacultyRecipient.school == School.school)  # Join the FacultyRecipient table on the school field
    .group_by(School.id, School.school_count)  # Group by School id and School's school_count
    .all()
)
    # Update each school's record in the database
    for row in result:
        school = db.query(School).filter(School.id == row.id).first()
        if school:
            school.repeat_faculty = row.repeat_faculty
            school.unique_faculty = row.unique_faculty

    db.commit()