import React, { useContext } from 'react';
import ReportPage from "../components/ReportPage";
import AuthContext from '../auth/AuthContext';

export default function GradStudentRecipients({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);
  const columnDefs = [
    { headerName: "Semester Taught", field: "semester_taught", filter: true, editable: isAuthenticated },
    { headerName: "Year Taught", field: "year_taught", filter: true, editable: isAuthenticated },
    { headerName: "Last Name", field: "last_name", filter: true, editable: isAuthenticated },
    { headerName: "First Name", field: "first_name", filter: true, editable: isAuthenticated },
    { headerName: "TA Email", field: "email", filter: true, editable: isAuthenticated },
    { headerName: "TA PID", field: "pid", filter: true, editable: isAuthenticated },
    { headerName: "Faculty Supervisor", field: "faculty_supervisor", filter: true, editable: isAuthenticated },
    { headerName: "School", field: "school", filter: true, editable: isAuthenticated },
    { headerName: "Department", field: "department", filter: true, editable: isAuthenticated },
    { headerName: "Course", field: "course", filter: true, editable: isAuthenticated },
    { headerName: "Number", field: "course_number", filter: true, editable: isAuthenticated },
    { headerName: "UNC Course Name", field: "unc_course_name", filter: true, editable: isAuthenticated },
    { headerName: "Partner Institution", field: "partner_institution", filter: true, editable: isAuthenticated },
    { headerName: "Award", field: "award", filter: true, editable: isAuthenticated },
  ];

  return (
    <ReportPage
      title="Graduate Students Recipients Page"
      fetchEndpoint="http://0.0.0.0:8080/gradstudent-recipient/gradstudent-recipient/"
      updateEndpoint="http://0.0.0.0:8080/gradstudent-recipient/update-recipient"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}