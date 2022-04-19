import React from 'react';
import './footer.css';

import Grid from '@mui/material/Grid';

import LocalPoliceIcon from '@mui/icons-material/LocalPolice';

const Footer = (props) => (
    <div className="footer" style={{height: "100%",  paddingRight: "20px"}}>
        <Grid container justifyContent="flex-end" sx={{mx: 2, width:"100%"}}>
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
    </div>
)

export default Footer;