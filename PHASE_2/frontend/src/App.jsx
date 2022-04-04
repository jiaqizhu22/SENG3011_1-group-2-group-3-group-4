import './App.css';
import React from 'react';

import Header from './components/header/header.jsx';
import SearchBar from './components/searchBar/searchBar.jsx';
import ArticleList from './components/container/article';

class MainApp extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      articles: []
    }
  }

  setArticles(artList) {
    this.setState({articles: artList});
    console.log(artList.length);
  }

  render() {
    return (
      <div className="App">
        <Header />
        <SearchBar setArticles={this.setArticles.bind(this)}/>
        <header className="App-header">
  
          {this.state.articles}
          
  
        </header>
      </div>
    );
  }
}

function App() {
  return (
    <MainApp />
  );
}

export default App;
