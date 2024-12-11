import React, { useContext } from 'react';
import ReportPage from '../components/ReportPage';
import AuthContext from '../auth/AuthContext';

export default function SummarySchools({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);

  const columnDefs = [
    { headerName: "School", field: "school", filter: true, editable: true },
    { headerName: "School Count", field: "school_count", filter: true, editable: true },
    { headerName: "Repeat Faculty", field: "repeat_faculty", filter: true, editable: true },
    { headerName: "Unique Faculty", field: "unique_faculty", filter: true, editable: true },
  ];

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL; // Base API URL from environment variables
  console.log("apibase: "+API_BASE_URL);
  const fetchEndpoint = `${API_BASE_URL}/school-dept/schools_table`;
  const updateEndpoint = `${API_BASE_URL}/school-dept/update-school`;
  const createEndpoint = `${API_BASE_URL}/school-dept/schools`;
  const largestId = `${API_BASE_URL}/school-dept/largest-id/school`;
  const deleteEndpoint = `${API_BASE_URL}/school-dept/delete-school`;

  return (
    <ReportPage
      title="Schools Data Page"
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
