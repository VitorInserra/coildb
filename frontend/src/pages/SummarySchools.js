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

  const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;
  const fetchEndpoint = `${API_BASE_URL}/school-dept/schools_table`;
  const updateEndpoint = `${API_BASE_URL}/schools/update-school`;

  return (
    <ReportPage
      title="Schools Data Page"
      fetchEndpoint="http://0.0.0.0:8080/school-dept/schools_table" 
      updateEndpoint="http://0.0.0.0:8080/school-dept/update-school" 
      createEndpoint="http://0.0.0.0:8080/school-dept/schools" 
      largestId="http://0.0.0.0:8080/school-dept/largest-id/school"
      deleteEndpoint="http://0.0.0.0:8080/school-dept/delete-school"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
