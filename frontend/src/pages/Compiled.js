import React from "react";
import ReportPage from "../components/ReportPage";

export default function CompiledQuantitativeDataPage({ addStarredReport }) {
  const columnDefs = [
    { headerName: "Semester", field: "semester", filter: true, editable: false },
    { headerName: "Offered Courses Count", field: "offered_courses_count", filter: true, editable: false },
    { headerName: "Co-Taught Courses Count", field: "cotaught_courses_count", filter: true, editable: false },
    { headerName: "Repeat Courses Count", field: "repeat_courses_count", filter: true, editable: false },
    { headerName: "Joint Courses Count", field: "joint_courses_count", filter: true, editable: false },
    { headerName: "New Courses Count", field: "new_courses_count", filter: true, editable: false },
    { headerName: "COIL Funding Awards Count", field: "coil_funding_awards_count", filter: true, editable: false },
    { headerName: "Unique Facility Count", field: "unique_facility_count", filter: true, editable: false },
    { headerName: "Graduate Award Count", field: "grad_award_count", filter: true, editable: false },
    { headerName: "Faculty Funding", field: "faculty_funding", filter: true, editable: false },
    { headerName: "Graduate Funding", field: "graduate_funding", filter: true, editable: false },
    { headerName: "Estimated UNC COIL Count", field: "estimated_UNC_coil_count", filter: true, editable: false },
    { headerName: "COIL Undergraduate FDOC Count", field: "coil_undergrad_fdoc_count", filter: true, editable: false },
    { headerName: "COIL Graduate FDOC Count", field: "coil_graduate_fdoc_count", filter: true, editable: false },
    { headerName: "COIL Students LDOC Count", field: "coil_students_ldoc_count", filter: true, editable: false },
    { headerName: "COIL Undergraduate LDOC Count", field: "coil_undergrad_ldoc_count", filter: true, editable: false },
    { headerName: "COIL Graduate LDOC Count", field: "coil_graduate_ldoc_count", filter: true, editable: false },
    { headerName: "Estimated Partner Student Count", field: "estimated_partnerstudent_count", filter: true, editable: false },
    { headerName: "Partner Country Count", field: "partner_country_count", filter: true, editable: false },
  ];

  return (
    <ReportPage
      title="Compiled Quantitative Data"
      fetchEndpoint="http://0.0.0.0:8080/compiled-data/get-quantity-data"
      updateEndpoint="http://0.0.0.0:8080/compiled-data/update-hard-coded"
      createEndpoint="http://0.0.0.0:8080/compiled-data/add-hard-coded"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
    />
  );
}
