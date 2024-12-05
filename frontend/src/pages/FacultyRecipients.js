import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css'; // Core grid CSS
import 'ag-grid-community/styles/ag-theme-alpine.css'; // Theme


export default function FacultyRecipients({ addStarredReport }) {
  const [showInput, setShowInput] = useState(false);
  const [title, setTitle] = useState("");
  const [rowData, setRowData] = useState([]); // holds backend data
  const navigate = useNavigate();

  // Fetching data from the backend
  useEffect(() => {
    fetch('http://0.0.0.0:8080/faculty-recipient/get-recipient') // Update to match your backend endpoint URL
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log(data)
        setRowData(data); // Set the fetched data to the grid
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const handleAddReport = () => {
    addStarredReport({ title, path: "/faculty-recipients" });
    setTitle("");
    setShowInput(false);
  };

  // TODO: define columnDefs by pulling straight from the backend
  const columnDefs = [
    { headerName: 'Last Name', field: 'last_name', filter: true },
    { headerName: 'First Name', field: 'first_name', filter: true },
    { headerName: 'Email', field: 'email', filter: true },
    { headerName: 'Department', field: 'department', filter: true },
    { headerName: 'School', field: 'school', filter: true },
    { headerName: 'Course Title', field: 'course_title', filter: true },
    { headerName: 'Course Number', field: 'course_number', filter: true },
    // Add other columns as needed based on the backend data
  ];

  return (
    <div>
      <h1>Faculty Recipients Page</h1>
      <button onClick={() => setShowInput(true)}>Star This Report</button>
      {showInput && (
        <div>
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            placeholder="Enter Title"
          />
          <button onClick={handleAddReport}>Add</button>
        </div>
      )}
      {/* Adding ag-Grid to display data */}
      <div className="ag-theme-alpine" style={{ height: 400, width: '100%' }}>
        <AgGridReact
          rowData={rowData}  // Data from backend
          columnDefs={columnDefs}  // Column definitions
          pagination={true}  // Optional: Add pagination for better display
          paginationPageSize={10}  // Optional: Number of rows per page
        />
      </div>
      <button onClick={() => navigate('/')}>Back to Homepage</button>
    </div>
  );
};
