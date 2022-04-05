import './App.css';
import React, {useState} from 'react';

import HeaderBar from './components/header/header'
import ArticleList from './components/articles/articleList';
import MapView from './components/map/mapView';
import SearchBar from './components/searchBar/searchBar'
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import ReactTooltip from "react-tooltip";


function App() {
    const [articles, setArticles] = useState([]);
    const [hoveringCountry, setHovering] = useState("");
    const [countryClicked, setCountry] = useState(null);

    return (
        <div className="App">
            <LocalizationProvider dateAdapter={AdapterDateFns}>
                <header>
                    <HeaderBar/>
                </header>

                <main>
                    <SearchBar setArticles={setArticles} setCountry={setCountry} country={countryClicked}/>
                    <ArticleList articles={articles} />
                    <MapView articles={articles} setHovering={setHovering} setCountry={setCountry}/>
                    <ReactTooltip>{hoveringCountry}</ReactTooltip>
                </main>
            </LocalizationProvider>
        </div>
    );
}

export default App;
