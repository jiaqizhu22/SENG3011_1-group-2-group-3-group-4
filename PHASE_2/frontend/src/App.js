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
         
      App 1 App 2 App 3
      </header>
    </div>
  );
}

export default App;
