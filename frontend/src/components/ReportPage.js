import React, { useState, useEffect, useRef, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AgGridReact } from 'ag-grid-react';
import 'ag-grid-community/styles/ag-grid.css';
import 'ag-grid-community/styles/ag-theme-alpine.css';
import AuthContext from '../auth/AuthContext';

export default function ReportPage({
  title,
  fetchEndpoint,
  updateEndpoint,
  createEndpoint,
  columnDefs,
  addStarredReport,
  largestId,
  deleteEndpoint,
}) {
  const [showInput, setShowInput] = useState(false);
  const [newReportTitle, setNewReportTitle] = useState("");
  const [rowData, setRowData] = useState([]);
  const navigate = useNavigate();
  const gridRef = useRef(null);
  const { isAuthenticated, authToken } = useContext(AuthContext);


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

  const handleAddStarredReport = () => {
    addStarredReport({ title: newReportTitle, path: window.location.pathname });
    setNewReportTitle("");
    setShowInput(false);
  };

  const handleInputChange = (field, value) => {
    const column = columnDefs.find((col) => col.field === field);
    setNewRowData((prev) => ({
        ...prev,
        [field]: column.type === "int"
            ? parseInt(value, 10) || 0
            : column.type === "boolean"
            ? value === "true" || value === true || value === false
            : value, // Default to string for "string" type
    }));
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
        'Authorization': `Basic ${authToken}`,
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

  const addRow = () => {
    fetch(largestId)
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to fetch largest ID: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        const max_id = data.largest_id || -5; 
        const newId = max_id + 1;             // Calculate the new ID
  
        const formattedData = columnDefs.reduce((acc, col) => {
          acc[col.field] = col.type === "boolean"
            ? newRowData[col.field] ?? false            //  false default for boolean
            : newRowData[col.field] ?? null;            //  null default
          return acc;
        }, { id: newId });
          
        console.log("Data being sent to backend:", formattedData); // Debugging log
  
        // Send the data to the backend
        fetch(createEndpoint, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify(formattedData),
        })
          .then((response) => {
            if (!response.ok) {
              throw new Error(`Failed to add row: ${response.statusText}`);
            }
            return response.json();
          })
          .then((newRow) => {
            setRowData((prev) => [...prev, newRow]); // Add the new row to the table
            setNewRowData({});                       // Reset the form
            setIsFormOpen(false);                    // Close the form
          })
          .catch((error) => console.error("Error adding row:", error));
      })
      .catch((error) => console.error("Error fetching largest ID:", error));
  };
  
  const [selectedRowId, setSelectedRowId] = useState(null);

  const handleRowClick = (event) => {
    const id = event.data.id; // Assuming `id` exists in your row data
    setSelectedRowId(id); // Save the selected row ID
    console.log("Selected Row ID:", id);
  };

  const handleDeleteRow = () => {
    if (!selectedRowId) {
      alert("Please select a row to delete.");
      return;
    }
    // Confirmation dialog (optional)
    const confirmDelete = window.confirm(`Are you sure you want to delete row with ID: ${selectedRowId}?`);

    if (!confirmDelete) return;

    fetch(`${deleteEndpoint}/${selectedRowId}`, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
      },
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Failed to delete row: ${response.statusText}`);
        }
        return response.json();
      })
      .then(() => {
        setRowData((prev) => prev.filter((row) => row.id !== selectedRowId));       // Remove the deleted row from the UI
        setSelectedRowId(null);
      })
      .catch((error) => console.error("Error deleting row:", error));
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
        <button
          style={{
            padding: "10px 20px",
            margin: "0 10px",
            backgroundColor: "#06693f", //"#4CAF50",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
          onClick={() => setIsFormOpen((prev) => !prev)} // Toggle the form
        >
          {isFormOpen ? "Cancel" : "Add New Row"}
        </button>
        <button
          style={{
            padding: "10px 20px",
            margin: "0 10px",
            backgroundColor: "#780707",
            color: "white",
            border: "none",
            borderRadius: "4px",
            cursor: "pointer",
          }}
          onClick={handleDeleteRow}
        >
          Delete Row
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
            onClick={handleAddStarredReport}
          >
            Add
          </button>
        </div>
      )}
      {/* Add New Row Form */}
      {isFormOpen && (
        <div
          style={{
            marginBottom: "20px",
            padding: "20px",
            border: "1px solid #ccc",
            borderRadius: "8px",
            width: "80%",
            margin: "0 auto",
          }}
        >
          <h3 style={{ textAlign: "center" }}>Add New Row</h3>
          {columnDefs.map((col) => (
            <div key={col.field} style={{ marginBottom: "10px" }}>
              <label style={{ marginRight: "10px" }}>{col.headerName}:</label>
              <input
                type={
                  col.type === "int"
                    ? "number"
                    : col.type === "boolean"
                    ? "checkbox"
                    : col.type === "date"
                    ? "date"
                    : "text"
                }          
                placeholder={col.headerName}
                value={newRowData[col.field] || ""}
                onChange={(e) => handleInputChange(col.field, e.target.value)}
                style={{
                  padding: "5px",
                  width: "200px",
                  border: "1px solid #ccc",
                  borderRadius: "4px",
                }}
              />
            </div>
          ))}
          <div style={{ textAlign: "center", marginTop: "20px" }}>
            <button
              onClick={addRow}
              style={{
                padding: "10px 20px",
                backgroundColor: "#06693f", //"#4CAF50",  4B9CD3
                color: "white",
                border: "none",
                borderRadius: "4px",
                cursor: "pointer",
              }}
            >
              Submit
            </button>
          </div>
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
          rowSelection="single" // Allow single-row selection
          onRowClicked={(event) => handleRowClick(event)} // Capture row click        
        />
      </div>
      <button
        onClick={() => navigate("/")}
        style={{
          padding: "10px 20px",
          marginTop: "20px",
          backgroundColor: "#13294B",
          color: "white",
          border: "none",
          borderRadius: "4px",
          cursor: "pointer",
          display: "block",
          marginLeft: "auto",
          marginRight: "auto",
        }}
      >
        Back to Homepage
      </button>
    </div>
  );
}