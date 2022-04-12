import './App.css';
import React, {useState} from 'react';

import HeaderBar from './components/header/header'
import ArticleList from './components/articles/articleList';
import MapView from './components/map/mapView';
import SearchBar from './components/searchBar/searchBar'
import BadgesModal from './components/modal/BadgesModal'

import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import ReactTooltip from "react-tooltip";
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';


function App() {
    const [articles, setArticles] = useState([]);
    const [hoveringCountry, setHovering] = useState("");
    const [countryClicked, setCountry] = useState(null);
    const [badgesOpen, setBadgesOpen] = useState(false);
    const [numSearches, setNumSearches] = useState(0);
    const [numArticleClicks, setNumArticleClicks] = useState(0);

    return (
        <div className="App" style={{height: "100%", width: "100%"}}>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
                <header style={{width: "100%"}}>
                    <HeaderBar openBadges={setBadgesOpen}/>
                </header>

                <main style={{height: "100%"}}>
                    <BadgesModal badgesOpen={badgesOpen} setBadgesOpen={setBadgesOpen} numSearches={numSearches} numArticleClicks={numArticleClicks}/>
                    <SearchBar setArticles={setArticles} setCountry={setCountry} country={countryClicked} numSearches={numSearches} setNumSearches={setNumSearches}/>
                    
                    <Stack direction="row" justifyContent="end" alignItems="flex-start" sx={{height: "80%", flexGrow: "1", flexShrink: "1", flexBasis: "auto"}}>
                        <ArticleList articles={articles} numArticleClicks={numArticleClicks} setNumArticleClicks={setNumArticleClicks}/>
                        <Divider orientation='vertical' />
                        <MapView articles={articles} setHovering={setHovering} setCountry={setCountry}/>
                    </Stack>
                    <ReactTooltip>{hoveringCountry}</ReactTooltip>
                </main>
            </LocalizationProvider>
        </div>
    );
}

export default App;
