import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css'; // Core grid CSS
import 'ag-grid-community/styles/ag-theme-alpine.css'; // Theme

export default function GradStudentRecipients({ addStarredReport }) {
    const [showInput, setShowInput] = useState(false);
    const [title, setTitle] = useState("");
    const [rowData, setRowData] = useState([]); // holds backend data
    const navigate = useNavigate();

    // Fetching data from the backend
  useEffect(() => {
    fetch('http://localhost:8080/gradstudent-recipient/gradstudent-recipient/') // Update to match your backend endpoint URL
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
      addStarredReport({ title, path: "/grad-student-recipients" });
      setTitle("");
      setShowInput(false);
    };

    const columnDefs = [
      { headerName: 'Semester Taught', field: 'semester_taught', filter: true },
      { headerName: 'Year Taught', field: 'year_taught', filter: true },
      { headerName: 'Last Name', field: 'last_name', filter: true },
      { headerName: 'First Name', field: 'first_name', filter: true },
      { headerName: 'TA Email or PID', field: 'ta_email_or_pid', filter: true },
      { headerName: 'Faculty Supervisor', field: 'faculty_supervisor', filter: true },
      { headerName: 'School', field: 'school', filter: true },
      { headerName: 'Department', field: 'department', filter: true },
      { headerName: 'Course', field: 'course', filter: true },
      { headerName: 'Number', field: 'course_number', filter: true },
      { headerName: 'UNC Course Name', field: 'unc_course_name', filter: true },
      { headerName: 'Partner Institution', field: 'partner_institution', filter: true },
      { headerName: 'Award', field: 'award', filter: true },
    ];
  
    return (
      <div>
        <h1>Grad Students Recipients Page</h1>
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

