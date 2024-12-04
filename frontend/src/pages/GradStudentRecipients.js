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
    fetch('http://0.0.0.0:8080/gradstudent-recipient/gradstudent-recipient/') // Update to match your backend endpoint URL
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
      { headerName: 'Semester Taught', field: 'semester_taught', filter: true, editable: true  },
      { headerName: 'Year Taught', field: 'year_taught', filter: true, editable: true  },
      { headerName: 'Last Name', field: 'last_name', filter: true, editable: true  },
      { headerName: 'First Name', field: 'first_name', filter: true, editable: true  },
      { headerName: 'TA Email or PID', field: 'ta_email_or_pid', filter: true, editable: true  },
      { headerName: 'Faculty Supervisor', field: 'faculty_supervisor', filter: true, editable: true  },
      { headerName: 'School', field: 'school', filter: true, editable: true  },
      { headerName: 'Department', field: 'department', filter: true, editable: true  },
      { headerName: 'Course', field: 'course', filter: true, editable: true  },
      { headerName: 'Number', field: 'course_number', filter: true, editable: true  },
      { headerName: 'UNC Course Name', field: 'unc_course_name', filter: true, editable: true  },
      { headerName: 'Partner Institution', field: 'partner_institution', filter: true, editable: true  },
      { headerName: 'Award', field: 'award', filter: true, editable: true  },
    ];

    const handleCellValueChanged = (event) => {
      const updatedData = event.data; // The updated row data
      console.log("Updated Row Data:", updatedData);
    
      // Call the backend to save the updated data
      saveUpdatedData(updatedData);
    };

    const saveUpdatedData = (updatedData) => {
      console.log("Data being sent:", updatedData);
      fetch(`http://0.0.0.0:8080/gradstudent-recipient/update-recipient`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedData), // Ensure the updatedData object matches the backend schema
      })
        .then(response => {
          if (!response.ok) {
            throw new Error(`Failed to save data: ${response.statusText}`);
          }
          return response.json();
        })
        .then(data => {
          console.log("Data successfully saved:", data);
        })
        .catch(error => console.error("Error saving data:", error));
    };    
  
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
            onCellValueChanged={handleCellValueChanged} // Capture changes
          />
        </div>
        <button onClick={() => navigate('/')}>Back to Homepage</button>
      </div>
    );
};

