import React, { useContext } from 'react';
import ReportPage from '../components/ReportPage';
import AuthContext from '../auth/AuthContext';

export default function SummarySchools({ addStarredReport }) {
  const { isAuthenticated, authToken } = useContext(AuthContext);

  const columnDefs = [
    { headerName: "School", field: "school", filter: true, editable: isAuthenticated },
    { headerName: "School Count", field: "school_count", filter: true, editable: isAuthenticated },
    { headerName: "Repeat Faculty", field: "repeat_faculty", filter: true, editable: isAuthenticated },
    { headerName: "Unique Faculty", field: "unique_faculty", filter: true, editable: isAuthenticated },
  ];

  return (
    <ReportPage
      title="Schools Data Page"
      fetchEndpoint="http://0.0.0.0:8080/school-dept/schools_table"
      updateEndpoint="http://0.0.0.0:8080/schools/update-school"
      columnDefs={columnDefs}
      addStarredReport={addStarredReport}
      authToken={authToken}
    />
  );
}
