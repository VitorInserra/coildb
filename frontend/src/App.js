import React, {useState} from 'react';
import Navbar from './components/Navbar'; 
import KeyStatistics from './components/KeyStatistics'; 
import PageCard from './components/PageCard'; 
import './index.css'; // Import your custom styles

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
        {/* Summary Reports PageCard */}
      <PageCard
        heading="Summary Reports"
        placeholder="Search Summary Reports..."
        value={searchSummaryReports}
        searchResult={setSearchSummaryReports}
        filteredReports={filteredSummaryReports}
      />

      {/* Starred Reports PageCard */}
      <PageCard
        heading="Starred Reports"
        placeholder="Search Starred Reports..."
        value={searchTermReports}
        searchResult={setSearchTermReports}
        filteredReports={filteredReports}
      />

      {/* Pages PageCard */}
      <PageCard
        heading="Pages"
        placeholder="Search Pages..."
        value={searchTerm}
        searchResult={setSearchTerm}
        filteredReports={filteredPages}
      />
      </div></>
  );
};

export default App;
