import React, {useState} from 'react';
import Navbar from './components/Navbar'; 
import KeyStatistics from './components/KeyStatistics'; 
import './App.css'; // Import your custom styles

const App = () => {
  // State to store the search query
  const [searchTerm, setSearchTerm] = useState('');
  const [searchTermReports, setSearchTermReports] = useState('');
  const [searchSummaryReports, setSearchSummaryReports] = useState('');

  // data which we should replace with our DB
  const pages = [
    "Faculty Recipients",
    "Grad Student Recipients",
    "Faculty Awarded But Canceled"
  ];

  const starredReports = [
    "Coil Courses Fall 2024",
    "Faculty Recipients Fall 2024"
  ];

  const summaryReports = [
    "Departmental", 
    "Schools", 
    "Compiled Quantitative Data"
  ];

  // Filter the pages based on the search term
  const filteredPages = pages.filter(page =>
    page.toLowerCase().includes(searchTerm.toLowerCase())
  );

  // Filter the starred reports based on the search term
  const filteredReports = starredReports.filter(report =>
    report.toLowerCase().includes(searchTermReports.toLowerCase())
  );

  // Filter the starred reports based on the search term
  const filteredSummaryReports = summaryReports.filter(report =>
    report.toLowerCase().includes(searchSummaryReports.toLowerCase())
  );

  return (
    <><div className="container">
        <Navbar />
        <header className="header">
          <h1>COIL Database</h1>
        </header>
        <KeyStatistics />
        <div className="content">
          <div className="summary-reports">
            <h2>Summary Reports</h2>
            {/* Search bar for Summary Reports */}
            <input
              type="text"
              placeholder="Search Summary Reports..."
              value={searchSummaryReports}
              onChange={(e) => setSearchSummaryReports(e.target.value)}
              className="search-bar" />

            <ul>
              {filteredSummaryReports.length > 0 ? (
                filteredSummaryReports.map((report, index) => (
                  <li key={index}>{report}</li>
                ))
              ) : (
                <li>No matching reports found</li>
              )}
            </ul>
          </div>

          <div className="starred-reports">
            <h2>Starred Reports</h2>

            {/* Search bar for Starred Reports */}
            <input
              type="text"
              placeholder="Search Starred Reports..."
              value={searchTermReports}
              onChange={(e) => setSearchTermReports(e.target.value)}
              className="search-bar" />

            <ul>
              {filteredReports.length > 0 ? (
                filteredReports.map((report, index) => (
                  <li key={index}>{report}</li>
                ))
              ) : (
                <li>No matching reports found</li>
              )}
            </ul>
          </div>

          <div className="pages">
            <h2>Pages</h2>
            {/* Search bar */}
            <input
              type="text"
              placeholder="Search Pages..."
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value)}
              className="search-bar" />

            <ul>
              {filteredPages.length > 0 ? (
                filteredPages.map((page, index) => (
                  <li key={index}>{page}</li>
                ))
              ) : (
                <li>No matching pages found</li>
              )}
            </ul>
          </div>
        </div>
      </div></>
  );
};

export default App;
