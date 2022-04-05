import './App.css';
import React, {useState} from 'react';

import HeaderBar from './components/header/header'
import ArticleList from './components/articles/articleList';
import MapView from './components/map/mapView';
import SearchBar from './components/searchBar/searchBar'
import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import ReactTooltip from "react-tooltip";
import Stack from '@mui/material/Stack';


function App() {
    const [articles, setArticles] = useState([]);
    const [hoveringCountry, setHovering] = useState("");
    const [countryClicked, setCountry] = useState(null);

    return (
        <div className="App" style={{height: "100%"}}>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
                <header>
                    <HeaderBar/>
                </header>

                <main style={{height: "100%"}}>
                    <SearchBar setArticles={setArticles} setCountry={setCountry} country={countryClicked}/>
                    
                    <Stack direction="row" justifyContent="end" alignItems="flex-start" sx={{height: "80%", flexGrow: "1", flexShrink: "1", flexBasis: "auto"}}>
                        <ArticleList articles={articles} />
                        <MapView articles={articles} setHovering={setHovering} setCountry={setCountry}/>
                    </Stack>
                    <ReactTooltip>{hoveringCountry}</ReactTooltip>
                </main>
            </LocalizationProvider>
        </div>
    );
}

export default App;
