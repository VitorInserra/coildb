import React from "react"

export default function Navbar() {
  return (
    <>
    <nav className="nav">
      <img src="/images/gflogowhite.png" className="nav--logo" alt="UNC Global Affairs Logo" />
      <h1 className="header-title">UNC COIL Database</h1>
      </nav>
      <img 
        src="/images/banner9.png" 
        alt="Global Network Banner" 
        className="header-banner" 
      />
    </>
  );
}