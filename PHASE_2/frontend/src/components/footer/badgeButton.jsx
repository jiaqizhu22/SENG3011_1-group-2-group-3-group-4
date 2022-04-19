import React from 'react';
import './footer.css';

import Grid from '@mui/material/Grid';

import LocalPoliceIcon from '@mui/icons-material/LocalPolice';

const BadgeButton = (props) => (
    
    <Grid >
        <button className="badgesButton"
            onClick={() => {
                props.openBadges(true);
            }}
        >
                <LocalPoliceIcon/>

                <span style={{paddingLeft: "10px"}}>
                    Badges
                </span>
        </button>
    </Grid>

)

export default BadgeButton;