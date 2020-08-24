import React from 'react';
import {FaTags} from 'react-icons/fa';

export const Navbar = ()=>{
  return (
    <nav className="navbar navbar-light bg-light mb-5 d-flex justify-content-center">
      <h1 className="text-center">
        <FaTags /> Price Tracker
      </h1>
    </nav>
  );
}