import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

import "./App.scss";

document.body.innerHTML = '<div id="root"></div>';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);