import React, { useContext } from 'react';
import ReportPage from '../components/ReportPage';
import AuthContext from '../auth/AuthContext';

export default function FacultyRecipients({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);

  const columnDefs = [
    { headerName: 'Last Name', field: 'last_name', filter: true, editable: isAuthenticated },
    { headerName: 'First Name', field: 'first_name', filter: true, editable: isAuthenticated },
    { headerName: 'Email', field: 'email', filter: true, editable: isAuthenticated },
    { headerName: 'Department', field: 'department', filter: true, editable: isAuthenticated },
    { headerName: 'School', field: 'school', filter: true, editable: isAuthenticated },
    { headerName: 'Course Title', field: 'course_title', filter: true, editable: isAuthenticated },
    { headerName: 'Course Number', field: 'course_number', filter: true, editable: isAuthenticated },
  ];

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
  const fetchEndpoint = `${API_BASE_URL}/faculty-recipient/get-recipient`;
  const updateEndpoint = `${API_BASE_URL}/faculty-recipient/update-recipient`;

  return (
    <ReportPage
      title="Faculty Recipients Page"
      fetchEndpoint={fetchEndpoint}
      updateEndpoint={updateEndpoint}
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
