import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css'; // Core grid CSS
import 'ag-grid-community/styles/ag-theme-alpine.css'; // Theme

export default function ReportPage({
  title,
  fetchEndpoint,
  updateEndpoint,
  columnDefs,
  addStarredReport,
}) {
  const [showInput, setShowInput] = useState(false);
  const [newReportTitle, setNewReportTitle] = useState("");
  const [rowData, setRowData] = useState([]); // holds backend data
  const navigate = useNavigate();
  const gridRef = useRef(null); // Reference to the grid for API access

  // Fetching data from the backend
  useEffect(() => {
    fetch(fetchEndpoint) // Fetch data using the provided endpoint
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Fetched data:", data);
        setRowData(data); // Set the fetched data to the grid
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [fetchEndpoint]);

  const handleAddReport = () => {
    addStarredReport({ title: newReportTitle, path: window.location.pathname });
    setNewReportTitle("");
    setShowInput(false);
  };

  const handleCellValueChanged = (event) => {
    const updatedData = event.data; // The updated row data
    console.log("Updated Row Data:", updatedData);

    // Call the backend to save the updated data
    saveUpdatedData(updatedData);
  };

  const saveUpdatedData = (updatedData) => {
    console.log("Data being sent:", updatedData);
    fetch(updateEndpoint, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updatedData), // Ensure the updatedData object matches the backend schema
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to save data: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        console.log("Data successfully saved:", data);
      })
      .catch((error) => console.error("Error saving data:", error));
  };

  const exportToCsv = () => {
    gridRef.current.api.exportDataAsCsv(); // Use Ag-Grid's export API
  };

  return (
    <div>
      <h1 style={{ textAlign: "center", marginBottom: "20px" }}>{title}</h1>
      <div style={{ display: "flex", justifyContent: "center", marginBottom: "20px" }}>
        <button
          style={{
            padding: "10px 20px",
            margin: "0 10px",
            backgroundColor: "#13294B",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
          onClick={() => setShowInput(true)}
        >
          Star This Report
        </button>
        <button
          style={{
            padding: "10px 20px",
            margin: "0 10px",
            backgroundColor: "#13294B",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
          onClick={exportToCsv}
        >
          Export as CSV
        </button>
      </div>
      {showInput && (
        <div style={{ display: "flex", justifyContent: "center", marginBottom: "20px" }}>
          <input
            type="text"
            value={newReportTitle}
            onChange={(e) => setNewReportTitle(e.target.value)}
            placeholder="Enter Title"
            style={{
                padding: "5px 10px", 
                width: "200px", 
                marginRight: "10px",
                border: "1px solid #ccc",
                borderRadius: "4px",
            }}
          />
          <button
            style={{
                padding: "5px 10px", 
                backgroundColor: "#13294B",
                color: "white",
                border: "none",
                borderRadius: "4px",
                cursor: "pointer",
            }}
            onClick={handleAddReport}
          >
            Add
          </button>
        </div>
      )}
      <div className="ag-theme-alpine" style={{ height: 400, width: "100%", margin: "0 auto" }}>
        <AgGridReact
          ref={gridRef}
          rowData={rowData} // Data from backend
          columnDefs={columnDefs} // Column definitions
          pagination={true} // Optional: Add pagination for better display
          paginationPageSize={10} // Optional: Number of rows per page
          onCellValueChanged={handleCellValueChanged} // Capture changes
        />
      </div>
      <button onClick={() => navigate('/')}>Back to Homepage</button>
    </div>
  );
}
