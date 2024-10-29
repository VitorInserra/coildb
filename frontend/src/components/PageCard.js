import React from "react";

export default function PageCard(props) {
    return (
        <div className="page-card">
            <h2 className="page-card-heading">{props.heading}</h2>
            {/* Search bar for Summary Reports */}
            <input
              type="text"
              placeholder={props.placeholder}
              value={props.value}
              onChange={(e) => props.searchResult(e.target.value)}
              className="search-bar" />

            <ul>
              {props.filteredReports.length > 0 ? (
                props.filteredReports.map((report, index) => (
                  <li key={index}>{report}</li>
                ))
              ) : (
                <li>No matching reports found</li>
              )}
            </ul>
          </div>
    )
}