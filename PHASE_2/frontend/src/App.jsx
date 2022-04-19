import './App.css';
import React, {useState} from 'react';
import 'react-notifications/lib/notifications.css';

import Header from './components/header/header'
import Footer from './components/footer/footer'
import ArticleList from './components/articles/articleList';
import MapView from './components/map/mapView';
import SearchBar from './components/searchBar/searchBar';
import BadgesModal from './components/modal/BadgesModal';
import TravelInfo from './components/travelinfo/travelInfo';
import TrackerModal from './components/modal/TrackerModal';
import TrackerButton from './components/footer/trakerButton';
import BadgesButton from './components/footer/badgeButton';

import AdapterDateFns from '@mui/lab/AdapterDateFns';
import LocalizationProvider from '@mui/lab/LocalizationProvider';
import ReactTooltip from "react-tooltip";
import Stack from '@mui/material/Stack';
import Divider from '@mui/material/Divider';
import {NotificationContainer, NotificationManager} from 'react-notifications';
import BadgeButton from './components/footer/badgeButton';


function App() {
    const [articles, setArticles] = useState([]);
    const [hoveringCountry, setHovering] = useState("");
    const [countryClicked, setCountry] = useState(null);
    const [badgesOpen, setBadgesOpen] = useState(false);
    const [numSearches, setNumSearches] = useState(0);
    const [numArticleClicks, setNumArticleClicks] = useState(0);
    const [travelInfo, setTravelInfo] = useState(null);
    const [trackerOpen, setTrackerOpen] = useState(false);

    function incrementSearches() {
        var newNumSearches = numSearches + 1;
        setNumSearches(newNumSearches);

        // Should probably move to its own place
        if (newNumSearches === 1) {
            NotificationManager.info("Achieved 'Searched once'!");
        }
        else if (newNumSearches === 5) {
            NotificationManager.info("Achieved 'Searched 5 Times'!");
        }
        else if (newNumSearches === 10) {
            NotificationManager.info("Achieved 'Searched 10 Times'!");
        }

        
    }

    function incrementArticleClicks() {
        var newNumArticleClicks = numArticleClicks + 1;
        setNumArticleClicks(newNumArticleClicks);

        if (newNumArticleClicks === 1) {
            NotificationManager.info("Achieved 'Visited one article'!");
        }
    
        if (newNumArticleClicks === 5) {
            NotificationManager.info("Achieved 'Visited 5 articles'!");
        }
    
        if (newNumArticleClicks === 10) {
            NotificationManager.info("Achieved 'Visited 10 articles'!");
        }
    }


    
    return (
        <div className="App" style={{height: "100%", width: "100%"}}>
            <LocalizationProvider dateAdapter={AdapterDateFns}>
                <header style={{width: "100%", display: "flex", height: "7%", top: "0", position: "fixed"}}>
                    <Header/>
                </header>
                
                <main style={{height: "85%", marginTop: "7%"}}>
                        <BadgesModal badgesOpen={badgesOpen} setBadgesOpen={setBadgesOpen} numSearches={numSearches} numArticleClicks={numArticleClicks}/>
                        <SearchBar setArticles={setArticles} setCountry={setCountry} country={countryClicked} incrementSearches={incrementSearches} setTravelInfo={setTravelInfo}/>
                        
                        <Stack direction="row" justifyContent="end" alignItems="flex-start" sx={{height: "90%", flexGrow: "1", flexShrink: "1", flexBasis: "auto"}}>
                            <ArticleList articles={articles} incrementArticleClicks={incrementArticleClicks}/>
                            <Divider orientation='vertical' />
                            <MapView articles={articles} setHovering={setHovering} setCountry={setCountry}/>
                        </Stack>
                        <ReactTooltip>{hoveringCountry}</ReactTooltip>

                        <TravelInfo travelInfo={travelInfo}/>
                </main>

                <footer className="footer" style={{height: "8%",  paddingRight: "6px"}}>
                        <BadgeButton openBadges={setBadgesOpen}/>
                        <TrackerButton openTracker={setTrackerOpen}/>
                </footer>
                

                <NotificationContainer/>

                
            </LocalizationProvider>

            
        </div>
    );
}

export default App;
