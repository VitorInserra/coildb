import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [authToken, setAuthToken] = useState(() => localStorage.getItem('authToken'));
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        if (authToken) {
            // Validate the token with the backend
            fetch('/ping', {
                headers: {
                    'Authorization': `Basic ${authToken}`,
                },
            })
                .then(res => {
                    if (res.ok) {
                        setIsAuthenticated(true);
                    } else {
                        setIsAuthenticated(false);
                        setAuthToken(null);
                        localStorage.removeItem('authToken');
                    }
                })
                .catch(() => {
                    setIsAuthenticated(false);
                    setAuthToken(null);
                    localStorage.removeItem('authToken');
                });
        } else {
            setIsAuthenticated(false);
        }
    }, [authToken]);

    const login = async (username, password) => {
        const token = btoa(`${username}:${password}`);
        localStorage.setItem('authToken', token);
        setAuthToken(token);
        setIsAuthenticated(true);
            return true;
    };

    const logout = () => {
        localStorage.removeItem('authToken');
        setAuthToken(null);
        setIsAuthenticated(false);
    };

    return (
        <AuthContext.Provider value={{ authToken, isAuthenticated, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

export default AuthContext;