import './travelInfo.css';
import React from 'react';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';

/*
{
  "country": "Algeria",
  "overview": {
    "open_status": "Partially Open",
    "quarantine_days": "Up to 14 Days"
  },
  "new_cases": "12",
  "new_percentage": "-66.67% (last 7 days)",
  "active_cases": "53,911",
  "active_percentage": "7.67% (last 7 days)",
  "can_you_enter": "Entry is restricted to ...",
  "what_to_expect": {
    "before_your_trip": "You must obtain advance ...",
    "on_arrival": "On arrival you will be required to ...",
    "quarantine_details": "There is no current quarantine requirement.",
    "travel_restrictions": "There are no routes that have greater restrictions at this time."
  }
}
*/

function denormaliseCountry(str) {
    const words = str.split("-");

    for (let i = 0; i < words.length; i++) {
        words[i] = words[i][0].toUpperCase() + words[i].substr(1);
    }

    return words.join(" ");
}

const TravelInfo = (props) => {
    if (props.travelInfo === null) {
        return null;
    }

    if (!props.travelInfo.hasOwnProperty("country"))
        return null; // No data found

    var overviewVal = null;
    if (props.travelInfo.hasOwnProperty("overview")) {
        overviewVal = (
            <div>
                <div className="infoSubTitle">
                    Overview:
                </div>

                <Grid container spacing={2} sx={{padding: "10px"}}>
                    <Grid item xs={5} sx={{padding: "10px"}}>
                        <b>Open status:</b> <br/> {props.travelInfo.overview.open_status}
                    </Grid>
                    <Grid item xs={5} sx={{padding: "10px"}}>
                        <b>Quarantine:</b> <br/> {props.travelInfo.overview.quarantine_days}
                    </Grid>
                </Grid>
                
                <br/>
                
            </div>
        );
    }

    var whatToExpect = null;
    if (props.travelInfo.hasOwnProperty("what_to_expect")) {
        whatToExpect = (
            <Grid container spacing={2} sx={{padding: "10px", width: "100%", flexGrow: "1", marginTop: "20px", marginBottom: "5%"}}>
                <Grid item xs={11} sx={{padding: "10px"}} className="overviewInfo">
                    <div className="infoSubTitle">
                        What to expect:
                    </div>

                    <div style={{padding: "10px"}}>
                        <div className="infoSubSubTitle">
                            Before your trip:
                        </div>

                        <div style={{padding: "10px"}}>
                            {props.travelInfo.what_to_expect.before_your_trip}
                        </div>
                    </div>

                    <div style={{padding: "10px"}}>
                        <div className="infoSubSubTitle">
                            On arrival:
                        </div>

                        <div style={{padding: "10px"}}>
                            {props.travelInfo.what_to_expect.on_arrival}
                        </div>
                    </div>

                    <div style={{padding: "10px"}}>
                        <div className="infoSubSubTitle">
                            Quarantine details:
                        </div>

                        <div style={{padding: "10px"}}>
                            {props.travelInfo.what_to_expect.quarantine_details}
                        </div>
                    </div>

                    <div style={{padding: "10px"}}>
                        <div className="infoSubSubTitle">
                            Travel restrictions:
                        </div>

                        <div style={{padding: "10px"}}>
                            {props.travelInfo.what_to_expect.travel_restrictions}
                        </div>
                    </div>
                </Grid>
            </Grid>
        );
    }

    return (
        <div className="travelInfo" style={{width:"100%", padding: "20px"}}>
            <div className="infoTitle">
                Travel information for {denormaliseCountry(props.travelInfo.country)}:
            </div>
            <br/>
            
            <Grid container spacing={2} sx={{padding: "10px", width: "100%", flexGrow: "1"}}>
                <Grid item xs={5} sx={{padding: "10px"}} className="overviewInfo">
                {overviewVal}
                </Grid>
                <Grid item xs={6} sx={{marginLeft: "20px", padding: "10px", right: "10px"}} className="overviewInfo">

                    <div className="infoSubTitle">
                        COVID-19 Data:
                    </div>

                    <Grid container spacing={2} sx={{padding: 2}}>
                        <Grid item xs={6} sx={{padding: "10px"}}>
                            <b>New cases:</b> {props.travelInfo.new_cases} <br/><br/>
                            <b>New % Change:</b> {props.travelInfo.new_percentage}
                        </Grid>
                        <Grid item xs={6} sx={{padding: "10px"}}>    
                            <b>Active Cases:</b> {props.travelInfo.active_cases} <br/><br/>
                            <b>Active % Change:</b> {props.travelInfo.active_percentage}
                        </Grid>
                    </Grid>
                </Grid>
            </Grid>

            <Grid container spacing={2} sx={{padding: "10px", width: "100%", flexGrow: "1", marginTop: "20px"}}>
                <Grid item xs={11} sx={{padding: "10px"}} className="overviewInfo">
                    
                    <div className="infoSubTitle">
                        Entry Information:
                    </div>

                    <div style={{padding: "20px"}}>
                        {props.travelInfo.can_you_enter}
                    </div>
                </Grid>
            </Grid>       

            {whatToExpect}
            
        </div>
    );
}

export default TravelInfo;