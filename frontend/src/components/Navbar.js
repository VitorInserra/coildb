import React, { useContext } from "react";
import AuthContext from '../auth/AuthContext';
import PropTypes from 'prop-types';


export default function Navbar({ openLoginModal }) {
  const { isAuthenticated, logout } = useContext(AuthContext);

  return (
    <>
      <nav className="nav">
        <img src="/images/gflogowhite.png" className="nav--logo" alt="UNC Global Affairs Logo" />
        <h1 className="header-title">UNC COIL at Carolina Database</h1>
        <div>
          {isAuthenticated ? (
            <button onClick={logout}>Logout</button>
          ) : (
            <button onClick={openLoginModal}>Login</button>
          )}
        </div>
      </nav>
      <img
        src="/images/banner9.png"
        alt="Global Network Banner"
        className="header-banner"
      />
    </>
  );
}

Navbar.propTypes = {
  openLoginModal: PropTypes.func.isRequired,
};