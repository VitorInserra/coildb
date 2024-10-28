import React from 'react';
import './App.css'; // Import your custom styles

const App = () => {
  return (
    <div className="container">
      <header className="header">
        <h1>COIL Database</h1>
      </header>

      <div className="content">
        <div className="key-statistics">
          <h2>Key Statistics</h2>
          <ul>
            <li>Departments Participating: 28</li>
            <li>Courses Available: 100</li>
            <li>Participating Schools: 50</li>
            <li>Students Enrolled: 100</li>
          </ul>
        </div>

        <div className="starred-reports">
          <h2>Starred Reports</h2>
          <ul>
            <li>Coil Courses Fall 2024</li>
            <li>Faculty Recipients Fall 2024</li>
          </ul>
        </div>

        <div className="pages">
          <h2>Pages</h2>
          <ul>
            <li>Faculty Recipients</li>
            <li>Grad Student Recipients</li>
            <li>Faculty Awarded But Canceled</li>
          </ul>
        </div>
      </div>
    </div>
  );
};

export default App;
