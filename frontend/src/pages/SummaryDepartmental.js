import React, { useState } from 'react';

// Add 'addStarredReport' as a prop in the component function
export default function SummaryDepartmental({ addStarredReport }) {
  const [showInput, setShowInput] = useState(false);
  const [title, setTitle] = useState("");

  const handleAddReport = () => {
    // Use 'addStarredReport' prop here
    addStarredReport({ title, path: "/summary-departmental" });
    setTitle("");
    setShowInput(false);
  };

  return (
    <div>
      <h1>Departmental Summary Page</h1>
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
    </div>
  );
}
