import React from 'react';
import './header.css';

import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import Stack from '@mui/material/Stack';

const Header = (props) => (
    <div className="header" style={{width: "100%"}}>
        <img 
            className="photo"
            src="https://www.inside.unsw.edu.au/sites/default/files/inline-images/crest.jpg"
            alt="1 Group 2 Group 3 Group 4"
        />
            1 Group 2 Group 3 Group 4


        <Grid container justifyContent="flex-end" sx={{mx: 2, width:"10%"}}>
            <Button
                onClick={() => {
                    props.openBadges(true);
                }}
            >
                BADGES
            </Button>
        </Grid>
    </div>
)

export default Header;