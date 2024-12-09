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
  console.log("apibase: "+API_BASE_URL);
  const fetchEndpoint = `${API_BASE_URL}/school-dept/departments_table`;
  const updateEndpoint = `${API_BASE_URL}/school-dept/update-department`;
  const createEndpoint = `${API_BASE_URL}/school-dept/department`;
  const largestId = `${API_BASE_URL}/school-dept/largest-id/department`;
  const deleteEndpoint = `${API_BASE_URL}/school-dept/delete-department`;


  return (
    <ReportPage
      title="COIL Courses Data Page"
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
