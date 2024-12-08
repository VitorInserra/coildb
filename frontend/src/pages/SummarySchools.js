import React from "react";
import ReportPage from "../components/ReportPage";

export default function SummarySchools({ addStarredReport }) {
  const columnDefs = [
    { headerName: "School", field: "school", filter: true, editable: true },
    { headerName: "School Count", field: "school_count", filter: true, editable: true },
    { headerName: "Repeat Faculty", field: "repeat_faculty", filter: true, editable: true },
    { headerName: "Unique Faculty", field: "unique_faculty", filter: true, editable: true },
  ];

  return (
    <ReportPage
      title="Schools Data Page"
      fetchEndpoint="http://0.0.0.0:8080/school-dept/schools_table" 
      updateEndpoint="TODO:CREATE ENDPOINT" 
      createEndpoint="http://0.0.0.0:8080/school-dept/schools" 
      largestId="http://0.0.0.0:8080/school-dept/largest-id/school"
      deleteEndpoint="http://0.0.0.0:8080/school-dept/delete-school"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
    />
  );
}
