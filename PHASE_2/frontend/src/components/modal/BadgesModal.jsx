import React from 'react';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Modal, { ModalBody, ModalFooter, ModalHeader } from './Modal';
import LocalPoliceIcon from '@mui/icons-material/LocalPolice';

import { red, blue, pink, purple, teal, green, grey } from '@mui/material/colors';

const boxStyle = {
    m: 1,
    border: 1,
    width: '5rem',
    height: '5rem',
    padding: '10px'
  };

function createBadge(colorFamily, text) {
    return (
        <Grid item xs={2} sx={{padding: "10px"}}>
            <Box sx={{ ...boxStyle, borderRadius: 4, borderColor: colorFamily[500], bgcolor: colorFamily[100], color: colorFamily[700] }}>
                <LocalPoliceIcon sx={{color: colorFamily[700]}}/>
                <Divider/>
                {text}
            </Box>
        </Grid>
    );
}

function createBadges(numSearches, numArticleClicks) {
    var badges = []
    var colorFamily;

    // Disabled
    colorFamily = grey;

    if (numSearches > 0) {
        colorFamily = red;
    }

    badges.push(createBadge(colorFamily, "Searched once"));
    colorFamily = grey;

    if (numSearches >= 5) {
        colorFamily = blue;
    }

    badges.push(createBadge(colorFamily, "Searched 5 Times"));
    colorFamily = grey;

    if (numSearches >= 10) {
        colorFamily = pink;
    }

    badges.push(createBadge(colorFamily, "Searched 10 Times"));
    colorFamily = grey;

    if (numArticleClicks > 0) {
        colorFamily = purple;
    }

    badges.push(createBadge(colorFamily, "Visited one article"));
    colorFamily = grey;

    if (numArticleClicks >= 5) {
        colorFamily = teal;
    }

    badges.push(createBadge(colorFamily, "Visited 5 articles"));
    colorFamily = grey;

    if (numArticleClicks >= 10) {
        colorFamily = green;
    }

    badges.push(createBadge(colorFamily, "Visited 10 articles"));

    return badges;
}

const BadgesModal = (props) => {
    return (
        <Modal
            show={props.badgesOpen}
            setShow={props.setBadgesOpen}
            >
            <ModalHeader>
                <h2>Badges</h2>
            </ModalHeader>
            <ModalBody>
                <Grid container spacing={2} sx={{padding: 2}}> 
                    {createBadges(props.numSearches, props.numArticleClicks)}
                </Grid>
            </ModalBody>
        </Modal>
    );
}

export default BadgesModal;