import React from 'react';

import Grid from '@mui/material/Grid';
import Box from '@mui/material/Box';
import Divider from '@mui/material/Divider';
import Modal, { ModalBody, ModalFooter, ModalHeader } from './Modal';
import LocalPoliceIcon from '@mui/icons-material/LocalPolice';

const boxStyle = {
    bgcolor: 'background.paper',
    borderColor: 'text.primary',
    m: 1,
    border: 1,
    width: '5rem',
    height: '5rem',
    padding: '10px'
  };

function createBadges(numSearches, numArticleClicks) {
    var badges = []

    if (numSearches > 0) {
        badges.push(
            <Grid item xs={2} sx={{padding: "10px"}}>
                <Box sx={{ ...boxStyle, borderRadius: 4 }}>
                    <LocalPoliceIcon/>
                    <Divider/>
                    Searched once
                </Box>
            </Grid>
        )
    }

    if (numSearches >= 5) {
        badges.push(
            <Grid item xs={2}>
                <Box sx={{ ...boxStyle, borderRadius: 4 }}>
                    <LocalPoliceIcon/>
                    <Divider/>
                    Searched 5 Times
                </Box>
            </Grid>
        )
    }

    if (numSearches >= 10) {
        badges.push(
            <Grid item xs={2}>
                <Box sx={{ ...boxStyle, borderRadius: 4 }}>
                    <LocalPoliceIcon/>
                    <Divider/>
                    Searched 10 Times
                </Box>
            </Grid>
        )
    }

    if (numArticleClicks > 0) {
        badges.push(
            <Grid item xs={2} sx={{padding: "10px"}}>
                <Box sx={{ ...boxStyle, borderRadius: 4 }}>
                    <LocalPoliceIcon/>
                    <Divider/>
                    Visited one article
                </Box>
            </Grid>
        )
    }

    if (numArticleClicks >= 5) {
        badges.push(
            <Grid item xs={2}>
                <Box sx={{ ...boxStyle, borderRadius: 4 }}>
                    <LocalPoliceIcon/>
                    <Divider/>
                    Visited 5 articles
                </Box>
            </Grid>
        )
    }

    if (numArticleClicks >= 10) {
        badges.push(
            <Grid item xs={2}>
                <Box sx={{ ...boxStyle, borderRadius: 4 }}>
                    <LocalPoliceIcon/>
                    <Divider/>
                    Visited 10 articles
                </Box>
            </Grid>
        )
    }

    if (badges.length <= 0) {
        badges.push(
            <Grid item xs={12}>
                You have no badges yet.
            </Grid>
        )
    }

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