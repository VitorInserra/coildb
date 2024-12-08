import React, { useContext } from 'react';
import ReportPage from '../components/ReportPage';
import AuthContext from '../auth/AuthContext';

export default function SummaryDepartmental({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);

  const columnDefs = [
    { headerName: "Department", field: "department", filter: true, editable: isAuthenticated },
    { headerName: "Course", field: "course", filter: true, editable: isAuthenticated },
  ];

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
  const fetchEndpoint = `${API_BASE_URL}/school-dept/departments_table`;
  const updateEndpoint = `${API_BASE_URL}/departments/update-department`;


  return (
    <ReportPage
      title="Departments Data Page"
      fetchEndpoint="http://0.0.0.0:8080/school-dept/departments_table" 
      updateEndpoint="http://0.0.0.0:8080/school-dept/update-department" 
      createEndpoint="http://0.0.0.0:8080/school-dept/department" 
      largestId="http://0.0.0.0:8080/school-dept/largest-id/department"
      deleteEndpoint="http://0.0.0.0:8080/school-dept/delete-department"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
