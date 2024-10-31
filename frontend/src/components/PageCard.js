import React from "react";
import { useNavigate } from 'react-router-dom';

export default function PageCard(props) {
  const navigate = useNavigate();

  const handleItemClick = (path) => {
    navigate(path); // Use navigate to go to the specified path
  };

  return (
    <div className="page-card">
      <h2 className="page-card-heading">{props.heading}</h2>
      <input
        type="text"
        placeholder={props.placeholder}
        value={props.value}
        onChange={(e) => props.searchResult(e.target.value)}
        className="search-bar"
      />
      <ul>
        {props.filteredReports.length > 0 ? (
          props.filteredReports.map((report, index) => (
            <li
              key={index}
              onClick={() => handleItemClick(report.path)}
              style={{ cursor: 'pointer' }}
            >
              {report.name}
            </li>
          ))
        ) : (
          <li>No matching reports found</li>
        )}
      </ul>
    </div>
  );
}
