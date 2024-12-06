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

  return (
    <ReportPage
      title="Faculty Recipients Page"
      fetchEndpoint="http://0.0.0.0:8080/faculty-recipient/get-recipient"
      updateEndpoint="http://0.0.0.0:8080/faculty-recipient/update-recipient"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
