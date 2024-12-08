import React, { useContext } from 'react';
import ReportPage from '../components/ReportPage';
import AuthContext from '../auth/AuthContext';

export default function FacultyRecipients({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);

  const columnDefs = [
    { headerName: "Last Name", field: "last_name", filter: true, editable: true, type: "string" },
    { headerName: "First Name", field: "first_name", filter: true, editable: true, type: "string" },
    { headerName: "Email", field: "email", filter: true, editable: true, type: "string" },
    { headerName: "Semester Taught", field: "semester_taught", filter: true, editable: true, type: "string" },
    { headerName: "School", field: "school", filter: true, editable: true, type: "string" },
    { headerName: "Department", field: "department", filter: true, editable: true, type: "string" },
    { headerName: "Course Name", field: "course_name", filter: true, editable: true, type: "string" },
    { headerName: "Course Number", field: "course_number", filter: true, editable: true, type: "string" },
    { headerName: "Sections", field: "sections", filter: true, editable: true, type: "string" },
    { headerName: "Total Sections Taught", field: "total_sections_taught", filter: true, editable: true, type: "int" },
    { headerName: "Course Title", field: "course_title", filter: true, editable: true, type: "string" },
    { headerName: "Co-Taught Semester", field: "co_taught_semester", filter: true, editable: true, type: "string" },
    { headerName: "Co-Taught Year", field: "co_taught_year", filter: true, editable: true, type: "int" },
    { headerName: "Repeat Course Semester", field: "repeat_course_semester", filter: true, editable: true, type: "string" },
    { headerName: "Repeat Course Year", field: "repeat_course_year", filter: true, editable: true, type: "int" },
    { headerName: "Joint Course", field: "joint_course", filter: true, editable: true, type: "string" },
    { headerName: "Quarter", field: "quarter", filter: true, editable: true, type: "string" },
    { headerName: "Estimated UNC Students", field: "estimated_unc_students", filter: true, editable: true, type: "int" },
    { headerName: "Estimated Partner Students", field: "estimated_partner_students", filter: true, editable: true, type: "int" },
    { headerName: "UNC Students FDOC Count", field: "unc_students_fdoc_count", filter: true, editable: true, type: "int" },
    { headerName: "UNC Students LDOC Count", field: "unc_students_ldoc_count", filter: true, editable: true, type: "int" },
    { headerName: "Partner Institution 1", field: "partner_institution1", filter: true, editable: true, type: "string" },
    { headerName: "Partner Country 1", field: "partner_country1", filter: true, editable: true, type: "string" },
    { headerName: "Partner Faculty 1", field: "partner_faculty1", filter: true, editable: true, type: "string" },
    { headerName: "Partner Institution 2", field: "partner_institution2", filter: true, editable: true, type: "string" },
    { headerName: "Partner Country 2", field: "partner_country2", filter: true, editable: true, type: "string" },
    { headerName: "Partner Faculty 2", field: "partner_faculty2", filter: true, editable: true, type: "string" },
    { headerName: "Credit", field: "credit", filter: true, editable: true, type: "string" },
    { headerName: "Award Date", field: "award_date", filter: true, editable: true, type: "date" },
    { headerName: "Graduate Student", field: "graduate_student", filter: true, editable: true, type: "string" },
    { headerName: "Faculty Amount Rewarded", field: "faculty_amount_rewarded", filter: true, editable: true, type: "int" },
    { headerName: "Graduate Award Student Amount", field: "graduate_award_student_amount", filter: true, editable: true, type: "int" },
    { headerName: "Repeat Award", field: "repeat_award", filter: true, editable: true, type: "string" },
    { headerName: "Repeat Award Criteria", field: "repeat_award_criteria", filter: true, editable: true, type: "string" },
    { headerName: "COIL Champions", field: "coil_champions", filter: true, editable: true, type: "string" },
    { headerName: "Notes", field: "notes", filter: true, editable: true, type: "string" },
    { headerName: "Partner Region", field: "partner_region", filter: true, editable: true, type: "string" },
    { headerName: "Cancelled", field: "cancelled", filter: true, editable: true, type: "boolean" },
  ];
  

  return (
    <ReportPage
      title="Faculty Recipients Page"
      fetchEndpoint="http://0.0.0.0:8080/faculty-recipient/get-recipient"
      updateEndpoint="http://0.0.0.0:8080/faculty-recipient/update-recipient"
      createEndpoint="http://0.0.0.0:8080/faculty-recipient/post-recipient/"
      largestId="http://0.0.0.0:8080/faculty-recipient/largest-id"
      deleteEndpoint="http://0.0.0.0:8080/faculty-recipient/delete-recipient"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
