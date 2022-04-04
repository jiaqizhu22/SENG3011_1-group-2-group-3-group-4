import './App.css';
import React from 'react';

import Header from './components/header/header.jsx';
import SearchBar from './components/searchBar/searchBar.jsx';
import Crap from './components/container/crap';

function App() {
  return (
    <div className="App">
      <Header />
      <SearchBar />
      <header className="App-header">
         
        Results!
        <Crap />
        

      </header>
    </div>
  );
}

export default App;
