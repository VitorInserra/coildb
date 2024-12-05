import React from "react";
import ReportPage from "../components/ReportPage";

export default function GradStudentRecipients({ addStarredReport }) {
  const columnDefs = [
    { headerName: "Semester Taught", field: "semester_taught", filter: true, editable: true },
    { headerName: "Year Taught", field: "year_taught", filter: true, editable: true },
    { headerName: "Last Name", field: "last_name", filter: true, editable: true },
    { headerName: "First Name", field: "first_name", filter: true, editable: true },
    { headerName: "TA Email", field: "email", filter: true, editable: true },
    { headerName: "TA PID", field: "pid", filter: true, editable: true },
    { headerName: "Faculty Supervisor", field: "faculty_supervisor", filter: true, editable: true },
    { headerName: "School", field: "school", filter: true, editable: true },
    { headerName: "Department", field: "department", filter: true, editable: true },
    { headerName: "Course", field: "course", filter: true, editable: true },
    { headerName: "Number", field: "course_number", filter: true, editable: true },
    { headerName: "UNC Course Name", field: "unc_course_name", filter: true, editable: true },
    { headerName: "Partner Institution", field: "partner_institution", filter: true, editable: true },
    { headerName: "Award", field: "award", filter: true, editable: true },
  ];

  return (
    <ReportPage
      title="Graduate Students Recipients Page"
      fetchEndpoint="http://0.0.0.0:8080/gradstudent-recipient/gradstudent-recipient/"
      updateEndpoint="http://0.0.0.0:8080/gradstudent-recipient/update-recipient"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
    />
  );
}