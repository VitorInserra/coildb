import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

export default function SummarySchools({ addStarredReport }) {
    const [showInput, setShowInput] = useState(false);
    const [title, setTitle] = useState("");
    const navigate = useNavigate();
  
    const handleAddReport = () => {
      addStarredReport({ title, path: "/summary-schools" });
      setTitle("");
      setShowInput(false);
    };
  
    return (
      <div>
        <h1>Schools Summary Page</h1>
        <button onClick={() => navigate('/')}>Back to Homepage</button>
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
