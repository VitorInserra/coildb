import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import PageCard from './components/PageCard';
import './index.css'; // Import your custom styles
import FacultyRecipients from './pages/FacultyRecipients';
import GradStudentRecipients from './pages/GradStudentRecipients';
import SummaryDepartmental from './pages/SummaryDepartmental';
import SummarySchools from './pages/SummarySchools';
import KeyStatistics from './components/KeyStatistics';

const App = () => {
  const [starredReports, setStarredReports] = useState([]);

  const addStarredReport = (report) => {
    setStarredReports((prevReports) => [...prevReports, report]);
  };

  return (
    <Router>
      <div className="container">
        <Navbar />
        <Routes>
          <Route path="/" element={<HomePage addStarredReport={addStarredReport} starredReports={starredReports} />} />
          <Route path="/faculty-recipients" element={<FacultyRecipients addStarredReport={addStarredReport}/>} />
          <Route path="/grad-student-recipients" element={<GradStudentRecipients addStarredReport={addStarredReport}/>} />
          <Route path="/summary-departmental" element={<SummaryDepartmental addStarredReport={addStarredReport} />} />
          <Route path="/summary-schools" element={<SummarySchools addStarredReport={addStarredReport} />} />
        </Routes>
        <footer className="blue-footer">
          <p>© 2024 The University of North Carolina at Chapel Hill</p>
        </footer>
      </div>
    </Router>
  );
};

const HomePage = ({ addStarredReport, starredReports }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [searchSummaryReports, setSearchSummaryReports] = useState('');
  const [searchTermStarred, setSearchTermStarred] = useState(''); // State for the Starred Reports search term

  const summaryReports = [
    { name: "Departmental", path: "/summary-departmental" },
    { name: "Schools", path: "/summary-schools" }
  ];

  const pages = [
    { name: "Faculty Recipients", path: "/faculty-recipients" },
    { name: "Grad Student Recipients", path: "/grad-student-recipients" },
  ];

  const filteredSummaryReports = summaryReports.filter(report =>
    report.name.toLowerCase().includes(searchSummaryReports.toLowerCase())
  );

  const filteredPages = pages.filter(page =>
    page.name.toLowerCase().includes(searchTerm.toLowerCase())
  );

  const filteredStarredReports = starredReports
    .filter(report => report.title.toLowerCase().includes(searchTermStarred.toLowerCase()))
    .map(report => ({ name: report.title, path: report.path }));

  return (
    <div>
    <KeyStatistics />
    <div className="content">
        <PageCard
          heading="Summary Reports"
          placeholder="Search Summary Reports..."
          value={searchSummaryReports}
          searchResult={setSearchSummaryReports}
          filteredReports={filteredSummaryReports}
        />
        <PageCard
          heading="Starred Reports"
          placeholder="Search Starred Reports..."
          value={searchTermStarred}
          searchResult={setSearchTermStarred} // Update search term state for Starred Reports
          filteredReports={filteredStarredReports} // Use the filtered Starred Reports
        />
        <PageCard
          heading="Pages"
          placeholder="Search Pages..."
          value={searchTerm}
          searchResult={setSearchTerm}
          filteredReports={filteredPages}
        />
    </div>
    </div>
  );
};


export default App;
