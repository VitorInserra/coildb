import React, { createContext, useState, useEffect } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [authToken, setAuthToken] = useState(() => localStorage.getItem('authToken'));
    const [isAuthenticated, setIsAuthenticated] = useState(false);

    useEffect(() => {
        if (authToken) {
            const API_BASE_URL = process.env.REACT_APP_API_BASE_URL
            console.log("Ping:", API_BASE_URL)
            fetch(`${API_BASE_URL}/ping`, {
                headers: {
                    'Authorization': `Basic ${authToken}`,
                    "Content-Type": "application/json",
                },
            }
            )
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
        const API_BASE_URL = process.env.REACT_APP_API_BASE_URL
        console.log("Ping:", API_BASE_URL)
        const response = await fetch(`${API_BASE_URL}/ping`, {
            headers: {
                'Authorization': `Basic ${token}`,
                "Content-Type": "application/json",
            },
        });

        if (response.ok) {
            localStorage.setItem('authToken', token);
            setAuthToken(token);
            setIsAuthenticated(true);
            return true;
        } else {
            throw new Error('Invalid credentials');
        }
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