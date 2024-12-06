import React from "react";
import ReportPage from "../components/ReportPage";

export default function FacultyRecipients({ addStarredReport }) {
  const columnDefs = [
    { headerName: "Last Name", field: "last_name", filter: true, editable: true },
    { headerName: "First Name", field: "first_name", filter: true, editable: true },
    { headerName: "Email", field: "email", filter: true, editable: true },
    { headerName: "Department", field: "department", filter: true, editable: true },
    { headerName: "School", field: "school", filter: true, editable: true },
    { headerName: "Course Title", field: "course_title", filter: true, editable: true },
    { headerName: "Course Number", field: "course_number", filter: true, editable: true },
  ];

  return (
    <ReportPage
      title="Faculty Recipients Page"
      fetchEndpoint="http://0.0.0.0:8080/faculty-recipient/get-recipient"
      updateEndpoint="http://0.0.0.0:8080/faculty-recipient/update-recipient"
      createEndpoint="http://0.0.0.0:8080/faculty-recipient/post-recipient/"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
    />
  );
}
