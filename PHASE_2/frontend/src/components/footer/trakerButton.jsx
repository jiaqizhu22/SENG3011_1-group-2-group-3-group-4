import React from 'react';
import './footer.css';

import Grid from '@mui/material/Grid';

import LocalPoliceIcon from '@mui/icons-material/LocalPolice';

const TrackerButton = (props) => (
    
    <Grid >
        <button className="badgesButton"
            onClick={() => {
                props.openTracker(true);
            }}
        >
                <LocalPoliceIcon/>

                <span style={{paddingLeft: "10px"}}>
                    COVID-19 Tracker
                </span>
        </button>
    </Grid>
    
)

export default TrackerButton;