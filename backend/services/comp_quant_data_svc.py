from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import text


class CompiledQuantitativeDataService:
    def full_query(self, db: Session, semester, year):
        query = f"""
SELECT
    -- Aggregated values from faculty
    COUNT(*) FILTER (
        WHERE f."Semester Taught" = :semester_year AND 
              f."Co-taught Semester" = :semester AND f."Co-taught Year" = :year
    ) AS coil_courses_offered,

    COUNT(*) FILTER (
        WHERE f."Semester Taught" = :semester_year AND 
              f."Co-taught Semester" = :semester AND f."Co-taught Year" = :year
    ) AS co_taught_courses,

    COUNT(*) FILTER (
        WHERE f."Repeat Course Semester" = :semester AND f."Repeat Course Year" = :year
    ) AS repeat_coil_courses,

    COUNT(*) FILTER (
        WHERE f."Joint - course" ILIKE :joint_filter
    ) AS joint_courses,

    COUNT(*) FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) - 
    COUNT(*) FILTER (
        WHERE f."Repeat Course Semester" = :semester AND f."Repeat Course Year" = :year
    ) AS new_coil_courses,

    COUNT(*) FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) - 
    COUNT(*) FILTER (
        WHERE f."Faculty Amount Awarded" IS NULL AND f."Semester Taught" = :semester_year
    ) AS coil_funding_awards,

    SUM(f."Faculty Amount Awarded") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS faculty_funding_pre_fring,

    SUM(f."Graduate Student Award Amount ") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS graduate_funding_pre_fring,

    SUM(f."Estimated UNC Students ") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS estimated_unc_students,

    c.undergrad_fdoc AS undergrad_fdoc,
    c.grad_fdoc AS grad_fdoc,
    c.undergrad_ldoc AS undergrad_ldoc,
    c.grad_ldoc AS grad_ldoc,
    c.eligible_ee_credit AS eligible_ee_credit,
    c.received_ee_credit AS received_ee_credit,


    -- Aggregated values from faculty
    SUM(f."Enrolled UNC Students (LDOC)") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS total_students_ldoc,
    
    SUM(f."Estimated Partner Students") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS estimated_partner_students,

    COUNT(DISTINCT f."Partner Institution 1") + COUNT(DISTINCT f."Partner Institution 2") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS partner_institutions,

    COUNT(DISTINCT f."Partner Country 1") + COUNT(DISTINCT f."Partner Country 2") FILTER (
        WHERE f."Semester Taught" = :semester_year
    ) AS partner_countries
FROM 
    faculty f
JOIN 
    compiled_hard c 
    ON c.semester = :semester_year
WHERE 
    f."Semester Taught" = :semester_year
GROUP BY
    c.undergrad_fdoc, 
    c.grad_fdoc, 
    c.undergrad_ldoc, 
    c.grad_ldoc, 
    c.eligible_ee_credit, 
    c.received_ee_credit;
        """

        result = (
            db.execute(
                text(query),
                {
                    "semester_year": f"{semester} {year}",
                    "semester": semester,
                    "year": year,
                    "joint_filter": f"%Joint: {semester} {year}%",
                },
            )
            .mappings()
            .fetchone()
        )

        return result
