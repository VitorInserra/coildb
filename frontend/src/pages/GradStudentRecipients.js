import React, { useContext } from 'react';
import ReportPage from "../components/ReportPage";
import AuthContext from '../auth/AuthContext';

export default function GradStudentRecipients({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);
  const columnDefs = [
    { headerName: "Semester Taught", field: "semester_taught", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "Year Taught", field: "year_taught", filter: true, editable: isAuthenticated, type: "int" },
    { headerName: "Last Name", field: "last_name", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "First Name", field: "first_name", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "TA Email", field: "email", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "TA PID", field: "pid", filter: true, editable: isAuthenticated, type: "int" },
    { headerName: "Faculty Supervisor", field: "faculty_supervisor", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "School", field: "school", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "Department", field: "department", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "Course", field: "course", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "Number", field: "number", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "UNC Course Name", field: "unc_course_name", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "Partner Institution", field: "partner_institution", filter: true, editable: isAuthenticated, type: "string" },
    { headerName: "Award", field: "award", filter: true, editable: isAuthenticated, type: "int" },
  ];

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
  const fetchEndpoint = `${API_BASE_URL}/gradstudent-recipient/gradstudent-recipient/`;
  const updateEndpoint = `${API_BASE_URL}/gradstudent-recipient/update-recipient`;
  const createEndpoint = `${API_BASE_URL}/gradstudent-recipient/gradstudent-recipient/`;
  const largestId = `${API_BASE_URL}/gradstudent-recipient/largest-id`;
  const deleteEndpoint = `${API_BASE_URL}gradstudent-recipient/delete-recipient`;

  return (
    <ReportPage
      title="Graduate Students Recipients Page"
      fetchEndpoint={fetchEndpoint}
      updateEndpoint={updateEndpoint}
      createEndpoint={createEndpoint}
      largestId={largestId}
      deleteEndpoint={deleteEndpoint}
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}