import './articles.css';
import React from 'react';

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import TravelExploreIcon from '@mui/icons-material/TravelExplore';
import { format } from 'date-fns'

function renderArticleEntry(url, date, headline) {
    return (
        <ListItem button component="a" href={url} target="_blank" rel="noopener noreferrer">
            <ListItemIcon>
                <TravelExploreIcon/>
            </ListItemIcon>
            <ListItemText
                primary={headline}
                secondary={date}
            />
        </ListItem>
    )
}

function ArticleList(props) {

    var articleEntries = [];
    for (var i = props.articles.length - 1; i >= 0; i--) {
        var obj = props.articles[i];

        var url = obj.article.url;
        var date = format(new Date(obj.article.date_of_publication), "yyyy-MM-dd");
        var headline = obj.article.headline;

        articleEntries.push(renderArticleEntry(url, date, headline));
    }

    

    return (
        <List sx={{ width: '100%', maxWidth: 360, bgcolor: 'background.paper' }}>
            {articleEntries}
        </List>
    );
}

export default ArticleList;