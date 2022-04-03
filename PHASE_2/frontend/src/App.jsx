import './App.css';
import React from 'react';

import Header from './components/header/header.jsx'
import SearchBar from './components/searchBar/searchBar.jsx'
function App() {
  return (
    <div className="App">
      <Header />
      <SearchBar />
      <header className="App-header">
         
      Results!

      <div id="crap">

      </div>

      </header>
    </div>
  );
}

export default App;
