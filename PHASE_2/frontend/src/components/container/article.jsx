import React from 'react';

const ArticleContainer = ( {url, date, headline, maintext, reports} ) => {
    console.log(url);

    return (
        <div className='article'>
            <h1>{headline}</h1>
            <h2>Date of publication: {date}</h2>
            <h2>Url: {url}</h2>
            <br/>
            <p>Main text: {maintext}</p>
            <br/>
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
        </div>
    );
};
export default ArticleContainer;