import React, { useState, useEffect, useRef } from 'react';
import { useNavigate } from 'react-router-dom';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';

export default function ReportPage({
  title,
  fetchEndpoint,
  updateEndpoint,
  columnDefs,
  addStarredReport,
}) {
  const [showInput, setShowInput] = useState(false);
  const [newReportTitle, setNewReportTitle] = useState("");
  const [rowData, setRowData] = useState([]);
  const navigate = useNavigate();
  const gridRef = useRef(null);


  useEffect(() => {
    fetch(fetchEndpoint)
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Fetched data:", data);
        setRowData(data);
      })
      .catch((error) => console.error("Error fetching data:", error));
  }, [fetchEndpoint]);

  const handleAddReport = () => {
    addStarredReport({ title: newReportTitle, path: window.location.pathname });
    setNewReportTitle("");
    setShowInput(false);
  };

  const handleCellValueChanged = (event) => {
    const updatedData = event.data;
    console.log("Updated Row Data:", updatedData);


    saveUpdatedData(updatedData);
  };

  const saveUpdatedData = (updatedData) => {
    console.log("Data being sent:", updatedData);
    fetch(updateEndpoint, {
      method: "PUT",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(updatedData),
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
    gridRef.current.api.exportDataAsCsv();
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
          rowData={rowData}
          columnDefs={columnDefs}
          pagination={true}
          paginationPageSize={10}
          onCellValueChanged={handleCellValueChanged}
        />
      </div>
      <button onClick={() => navigate('/')}>Back to Homepage</button>
    </div>
  );
}