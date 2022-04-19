import React from 'react';

import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import TravelExploreIcon from '@mui/icons-material/TravelExplore';
import Divider from '@mui/material/Divider';
import { format } from 'date-fns'

function renderArticleEntry(url, date, headline, incrementArticleClicks) {
    return (
        <ListItem button component="a" href={url} target="_blank" rel="noopener noreferrer"
            onClick={() => {
                incrementArticleClicks();
            }}
        >
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

        articleEntries.push(renderArticleEntry(url, date, headline, props.incrementArticleClicks));
        articleEntries.push(<Divider />);
    }

    

    return (
        <List sx={{ width: '20%', maxWidth: 360, height: "98%", maxHeight: 1.0, overflow: 'auto', bgcolor: 'background.paper' }}>
            {articleEntries}
        </List>
    );
}

export default ArticleList;