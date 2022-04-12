import React from 'react';

const ArticleContainer = ( {url, date, headline, main_text, reports} ) => {
    return (
        <div className='article'>
            <h1>{headline}</h1>
            <h2>Date of publication: {date}</h2>
            <h2>Url: {url}</h2>
            <br/>
            <p>Main text: {main_text}</p>
            <br/>
        </div>
    );
};

/* be careful putting this back in, it breaks stuff because location doesn't turn into a string properly
{reports.map((report) => (
                <div className='report'>
                    diseases: {report.diseases}
                    <br/>
                    syndromes: {report.syndromes}
                    <br/>
                    event_date: {report.event_date}
                    <br/>
                    location: {report.locations}
                    <br/>
                </div>
            ))}
*/

class ArticleList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
          articles: [],
        };
      }

    doRender() {
        console.log(this.state.articles);
        
    }
    
    render() {
        if (this.state.articles.length > 0)
            return this.state.articles[0];

        return null;
    }
}

const articleListSingleton = new ArticleList();
export {ArticleContainer, articleListSingleton};

export default ArticleList;