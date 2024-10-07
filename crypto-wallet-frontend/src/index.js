import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Get the root element in the HTML where we will mount our React app
const rootElement = document.getElementById('root');

// Create a root for React rendering
const root = ReactDOM.createRoot(rootElement);

// Render the main App component inside the root
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
