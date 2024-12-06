import React from "react";
import ReportPage from "../components/ReportPage";

export default function SummaryDepartmental({ addStarredReport }) {
  const columnDefs = [
    { headerName: "Department", field: "department", filter: true, editable: true },
    { headerName: "Course", field: "course", filter: true, editable: true },
  ];

  return (
    <ReportPage
      title="Departments Data Page"
      fetchEndpoint="http://0.0.0.0:8080/school-dept/departments_table" 
      updateEndpoint="http://0.0.0.0:8080/departments/update-department" 
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
    />
  );
}
