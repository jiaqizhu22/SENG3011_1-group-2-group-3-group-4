import './App.css';
import React from 'react';
import * as Loader from "react-loader-spinner";
import Header from './components/header/header.jsx';
import SearchBar from './components/searchBar/searchBar.jsx';
import ArticleList from './components/container/article';

const LoadingIndicator = props => {
   return (
    <h1 hidden = "true" id = "LoadingIndicator">Loading...</h1>
  );  
}
const NoResults = props => {
  return (
   <h1 hidden = "true" id = "NoResults">0 results matched your search criteria</h1>
 );  
}


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
    if(artList.length == 0){
      document.getElementById("NoResults").hidden = false;
    }
  }
//remove line 43 to remove score treacking. right now the user can get a score each time they do a successful search
  render() {
    return (
      <div className="App">
        
        <Header />
        <SearchBar setArticles={this.setArticles.bind(this)}/>
        <header className="App-header">
          Your current score is: {localStorage.getItem('userPoints')} 
          <LoadingIndicator/>
          <NoResults/>
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
