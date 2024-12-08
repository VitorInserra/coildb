import React, { useState, useContext, useEffect } from 'react';
import AuthContext from '../auth/AuthContext';
import PropTypes from 'prop-types';

const LoginModal = ({ isOpen, onClose }) => {
  const { login, isAuthenticated } = useContext(AuthContext);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState(null);


  useEffect(() => {
    if (isAuthenticated && isOpen) {
      onClose();
    }
  }, [isAuthenticated, isOpen, onClose]);

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      await login(username, password);

    } catch (err) {
      setError(err.message || 'Invalid credentials');
    }
  };

  if (!isOpen) return null;

  return (
    <div className="modal-overlay" style={modalOverlayStyle}>
      <div className="modal-content" style={modalContentStyle}>
        <h2>Please Login</h2>
        <form onSubmit={handleLogin}>
          <div style={{ marginBottom: '10px' }}>
            <label>Username: </label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div style={{ marginBottom: '10px' }}>
            <label>Password: </label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          {error && <p style={{ color: 'red' }}>{error}</p>}
          <button type="submit">Login</button>
          <button type="button" onClick={onClose} style={closeButtonStyle}>Cancel</button>
        </form>
      </div>
    </div>
  );
};

const modalOverlayStyle = {
  position: 'fixed',
  top: 0, left: 0, right: 0, bottom: 0,
  backgroundColor: 'rgba(0,0,0,0.5)',
  display: 'flex',
  justifyContent: 'center',
  alignItems: 'center',
  zIndex: 9999
};

const modalContentStyle = {
  background: '#fff',
  padding: '20px',
  borderRadius: '8px',
  minWidth: '300px'
};

const closeButtonStyle = {
  marginLeft: '10px',
  padding: '5px 10px',
  backgroundColor: '#ccc',
  color: 'black',
  border: 'none',
  borderRadius: '4px',
  cursor: 'pointer',
};

LoginModal.propTypes = {
  isOpen: PropTypes.bool.isRequired,
  onClose: PropTypes.func.isRequired,
};

export default LoginModal;
