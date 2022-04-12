import './map.css';
import React from 'react';
import {
    ComposableMap,
    Geographies,
    Geography,
    Marker,
    } from "react-simple-maps";

const geoUrl = "https://raw.githubusercontent.com/zcreativelabs/react-simple-maps/master/topojson-maps/world-110m.json";

function createMarkerCoords(reports) {
    var markers = [];

    for (var obj of reports) {
        for (var loc of obj.locations) {
            var lat = loc.lat;
            var lng = loc.lng;
            
            markers.push({coordinates: [parseFloat(lng), parseFloat(lat)]});
        }
    }

    return markers;
}

const rounded = num => {
    if (num > 1000000000) {
        return Math.round(num / 100000000) / 10 + "Bn";
    } else if (num > 1000000) {
        return Math.round(num / 100000) / 10 + "M";
    } else {
        return Math.round(num / 100) / 10 + "K";
    }
};

const MapView = (props) => {

    var markers = [];

    for (var i = props.articles.length - 1; i >= 0; i--) {
        var obj = props.articles[i];

        // Create marker list
        markers = markers.concat(createMarkerCoords(obj.article.reports));
    }

    return (
        <ComposableMap data-tip="" style={{width: "80%"}} projection="geoMercator" projectionConfig={{scale: 100}}>
            <Geographies geography={geoUrl}>
                {({ geographies }) =>
                    geographies
                    .map(geo => (
                        <Geography
                            key={geo.rsmKey}
                            geography={geo}
                            onMouseEnter={() => {
                                const { NAME, POP_EST } = geo.properties;
                                props.setHovering(`${NAME} — ${rounded(POP_EST)}`);
                            }}
                            onMouseLeave={() => {
                                props.setHovering("");
                            }}
                            onClick={() => {
                                const { NAME } = geo.properties;
                                props.setCountry(`${NAME}`);
                            }}

                            style={{
                                default: {
                                fill: "#D6D6DA",
                                    outline: "none"
                                },
                                hover: {
                                    fill: "#F53",
                                    outline: "none"
                                },
                                pressed: {
                                    fill: "#E42",
                                    outline: "none"
                                }
                            }}
                        />
                    ))
                }
                </Geographies>

                {markers.map(({ coordinates }) => (
                    <Marker coordinates={coordinates} style={{pointerEvents: "none"}}>
                        <circle r={10} fill="#F00" stroke="#fff" strokeWidth={2} />
                    </Marker>
                ))}

        </ComposableMap>
    );
}

export default MapView;