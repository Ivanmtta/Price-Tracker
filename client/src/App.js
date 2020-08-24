import React from 'react';
import './App.css';
import './bootstrap.min.css';

import {Navbar} from './components/Navbar'
import {PageContent} from './components/PageContent'

function App(){

  return (
    <div>
      <Navbar />
      <div className="container">
        <PageContent />
      </div>
    </div>
  );
}

export default App;