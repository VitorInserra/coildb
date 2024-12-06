import React, { useContext } from 'react';
import ReportPage from '../components/ReportPage';
import AuthContext from '../auth/AuthContext';

export default function SummaryDepartmental({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);

  const columnDefs = [
    { headerName: "Department", field: "department", filter: true, editable: isAuthenticated },
    { headerName: "Course", field: "course", filter: true, editable: isAuthenticated },
  ];

  return (
    <ReportPage
      title="Departments Data Page"
      fetchEndpoint="http://0.0.0.0:8080/school-dept/departments_table"
      updateEndpoint="http://0.0.0.0:8080/departments/update-department"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
