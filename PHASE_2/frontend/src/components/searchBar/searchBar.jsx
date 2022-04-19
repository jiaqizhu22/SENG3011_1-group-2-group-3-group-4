import './searchBar.css';

import React, {useState} from 'react';

import TextField from '@mui/material/TextField';
import DatePicker from '@mui/lab/DatePicker'
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import Button from '@mui/material/Button';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { format, subYears } from 'date-fns'

const apiFetch = (end_date, start_date, key_terms, location, setSearching, incrementSearches) => { 

    if (location == null || typeof location != "string" || location === "") {
        alert("Country cannot be empty.");
        return null;
    }

    if (end_date == null) {
        end_date = new Date();
    }

    if (start_date == null) {
        start_date = subYears(new Date(), 20); // Default to 20 years ago
    }

    if (key_terms == null || typeof location != "string" || key_terms === "") {
        key_terms = "outbreak";
    }

    end_date = format(end_date, "yyyy-MM-dd");
    start_date = format(start_date, "yyyy-MM-dd");
    
    var url = `https://seng3011-bobby-tables-backend.herokuapp.com/article?end_date=${end_date}T00%3A00%3A00&start_date=${start_date}T00%3A00%3A00&key_terms=${key_terms}&location=${location}&limit=1000&offset=0`;
    console.log(url);

    setSearching(true);
    
    return new Promise((resolve, reject) => {
        fetch(url)
        .then((response) => {
            if (response.status === 400 || response.status === 403) {
                response.json().then((errorMsg) => {
                    alert(errorMsg['error']);
                    reject(errorMsg['error']);
                });
            }else if(response.status === 200) {
                response.json().then(data => {
                    resolve(data);
                });
            } else {
                reject("Error: " + response.status + " response received!");
            }

            setSearching(false);
            incrementSearches();
        })
        .catch((err) => {
            setSearching(false);
            incrementSearches();
            console.log(err)
            resolve(null);
        });
    });
}


const SearchBar = (props) => {
    const [startDate, setStartDate] = useState(null);     
    const [endDate, setEndDate] = useState(null); 
    const [keyTerms, setKeyTerms] = useState(null); 
    const [searching, setSearching] = useState(false);

    const darkTheme = createTheme({
        palette: {
          mode: 'dark',
        },
      });

    return (
    <ThemeProvider theme={darkTheme}>
        <div className = "searchBar" style={{paddingTop: "1%", paddingBottom: "1%"}}>
            <TextField sx={{mx: 4, width:"30%"}} id="countrySearch" label="Country" variant="standard" 
            value={props.country}
            placeholder="Country"
            onChange={(event) => {
                const {value} = event.target;
                props.setCountry(value);
            }}
            InputLabelProps={{ shrink: true }}
            />
            <DatePicker
                clearable
                label="Start Date"
                value={startDate}
                format="dd-MM-yyyy"

                onChange={(newValue) => {
                    setStartDate(newValue);
                }}
                renderInput={(props) => <TextField sx={{width:"30%"}} {...props} />}
            />
            <Box sx={{mx: 2}}>to</Box>
            <DatePicker
                label="End Date"
                value={endDate}
                onChange={(newValue) => {
                    setEndDate(newValue);
                }}
                renderInput={(props) => <TextField sx={{width:"30%"}} {...props} />}
            />
            <TextField sx={{mx: 4, width:"50%"}} id="keyTerms" label="Key Terms (Separated by comma)" variant="standard" 
            value={keyTerms}
            onChange={(event) => {
                const {value} = event.target;
                setKeyTerms(value);
            }}
            />

            <Grid container justifyContent="flex-end" sx={{mx: 2, width:"10%"}}>
                <Button
                    disabled={searching}
                    onClick={() => {
                        var apiRet = apiFetch(endDate, startDate, keyTerms, props.country, setSearching, props.incrementSearches)

                        if (apiRet != null) {
                            apiRet.then((data) => {
                                if (data != null)
                                    props.setArticles(data.articles);
    
                                setSearching(false);
                            });
                        }
                    }
                }
                >
                    {searching?"Searching":"Search"}
                </Button>
            </Grid>
            
        </div>
    </ThemeProvider>
    );
}


export default SearchBar;