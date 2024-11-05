import React, { useState } from 'react';


export default function SummarySchools({ addStarredReport }) {
    const [showInput, setShowInput] = useState(false);
    const [title, setTitle] = useState("");
  
    const handleAddReport = () => {
      addStarredReport({ title, path: "/summary-schools" });
      setTitle("");
      setShowInput(false);
    };
  
    return (
      <div>
        <h1>Schools Summary Page</h1>
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
      </div>);
}
