from sqlalchemy import func, text
from sqlalchemy.orm import Session
from models.school_dept import School
from models.faculty_recipient import FacultyRecipient


def update_faculty_counts(db: Session):
    #Raw SQL query to update repeat_faculty field in the Schools table
   update_query = text("""
      -- Update repeat_faculty count for College of Arts & Sciences
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%College%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'College of Arts & Sciences';




-- Update repeat_faculty count for School of Nursing
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Nursing%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'School of Nursing';




-- Update repeat_faculty count for Kenan-Flagler Business School
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Business%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'Kenan-Flagler Business School';




-- Update repeat_faculty count for School of Education
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Education%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'School of Education';




-- Update repeat_faculty count for Hussman School of Journalism and Media
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Journalism%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'Hussman School of Journalism and Media';




-- Update repeat_faculty count for School of Government
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Government%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'School of Government';




-- Update repeat_faculty count for School of Medicine
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Medicine%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'School of Medicine';




-- Update repeat_faculty count for Gillings School of Global Public Health
UPDATE "schools"
SET "repeat_faculty" = (
  SELECT COUNT(*)
  FROM "faculty"
  WHERE "School" LIKE '%Public Health%'
    AND "Repeat Course Semester" IS NOT NULL
)
WHERE "school" = 'Gillings School of Global Public Health';
  """)

   # Execute the SQL query
   db.execute(update_query)
   # Raw SQL query to calculate unique_faculty
   unique_query = text("""
       UPDATE "schools"
       SET "unique_faculty" = "school_count" - "repeat_faculty";
   """)


   # Execute the unique faculty query
   db.execute(unique_query)


   db.commit()


   """result = (
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


   db.commit()"""
