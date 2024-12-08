import React from "react";
import ReportPage from "../components/ReportPage";

export default function GradStudentRecipients({ addStarredReport }) {
  const columnDefs = [
    { headerName: "Semester Taught", field: "semester_taught", filter: true, editable: true, type: "string" },
    { headerName: "Year Taught", field: "year_taught", filter: true, editable: true, type: "int" },
    { headerName: "Last Name", field: "last_name", filter: true, editable: true, type: "string" },
    { headerName: "First Name", field: "first_name", filter: true, editable: true, type: "string" },
    { headerName: "TA Email", field: "email", filter: true, editable: true, type: "string" },
    { headerName: "TA PID", field: "pid", filter: true, editable: true, type: "int" },
    { headerName: "Faculty Supervisor", field: "faculty_supervisor", filter: true, editable: true, type: "string" },
    { headerName: "School", field: "school", filter: true, editable: true, type: "string" },
    { headerName: "Department", field: "department", filter: true, editable: true, type: "string" },
    { headerName: "Course", field: "course", filter: true, editable: true, type: "string" },
    { headerName: "Number", field: "number", filter: true, editable: true, type: "string" },
    { headerName: "UNC Course Name", field: "unc_course_name", filter: true, editable: true, type: "string" },
    { headerName: "Partner Institution", field: "partner_institution", filter: true, editable: true, type: "string" },
    { headerName: "Award", field: "award", filter: true, editable: true, type: "int" },
  ];

  return (
    <ReportPage
      title="Graduate Students Recipients Page"
      fetchEndpoint="http://0.0.0.0:8080/gradstudent-recipient/gradstudent-recipient/"
      updateEndpoint="http://0.0.0.0:8080/gradstudent-recipient/update-recipient"
      createEndpoint="http://0.0.0.0:8080/gradstudent-recipient/gradstudent-recipient/"
      largestId="http://0.0.0.0:8080/gradstudent-recipient/largest-id"
      deleteEndpoint="http://0.0.0.0:8080/gradstudent-recipient/delete-recipient"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
    />
  );
}