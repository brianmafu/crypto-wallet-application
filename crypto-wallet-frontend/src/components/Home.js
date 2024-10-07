// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';

function Home() {
  return (
    <div>
      <h1>Welcome to Crypto Wallet</h1>
      <p>Please sign in or sign up to continue.</p>
      <Link to="/signin">Sign In</Link>
      <br />
      <Link to="/signup">Sign Up</Link>
    </div>
  );
}

export default Home;
