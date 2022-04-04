import React from 'react';
import './searchBar.css';
import {useState} from 'react';
import { DateRangePickerComponent } from '@syncfusion/ej2-react-calendars';
import { format } from "date-fns";
import apiFetch from '../../index.js';
import {ArticleContainer} from '../container/article';
//import ReportContainer from '../container/report';


const country_list = [
    "Afghanistan",
    "Albania",
    "Algeria",
    "Andorra",
    "Angola",
    "Antigua and Barbuda",
    "Argentina",
    "Armenia",
    "Australia",
    "Austria",
    "Azerbaijan",
    "The Bahamas",
    "Bahrain",
    "Bangladesh",
    "Barbados",
    "Belarus",
    "Belgium",
    "Belize",
    "Benin",
    "Bhutan",
    "Bolivia",
    "Bosnia and Herzegovina",
    "Botswana",
    "Brazil",
    "Brunei",
    "Bulgaria",
    "Burkina Faso",
    "Burundi",
    "Cabo Verde",
    "Cambodia",
    "Cameroon",
    "Canada",
    "Central African Republic",
    "Chad",
    "Chile",
    "China",
    "Colombia",
    "Comoros",
    "Congo, Democratic Republic of the",
    "Congo, Republic of the",
    "Costa Rica",
    "Côte d’Ivoire",
    "Croatia",
    "Cuba",
    "Cyprus",
    "Czech Republic",
    "Denmark",
    "Djibouti",
    "Dominica",
    "Dominican Republic",
    "East Timor (Timor-Leste)",
    "Ecuador",
    "Egypt",
    "El Salvador",
    "Equatorial Guinea",
    "Eritrea",
    "Estonia",
    "Eswatini",
    "Ethiopia",
    "Fiji",
    "Finland",
    "France",
    "Gabon",
    "The Gambia",
    "Georgia",
    "Germany",
    "Ghana",
    "Greece",
    "Grenada",
    "Guatemala",
    "Guinea",
    "Guinea-Bissau",
    "Guyana",
    "Haiti",
    "Honduras",
    "Hungary",
    "Iceland",
    "India",
    "Indonesia",
    "Iran",
    "Iraq",
    "Ireland",
    "Israel",
    "Italy",
    "Jamaica",
    "Japan",
    "Jordan",
    "Kazakhstan",
    "Kenya",
    "Kiribati",
    "Korea, North",
    "Korea, South",
    "Kosovo",
    "Kuwait",
    "Kyrgyzstan",
    "Laos",
    "Latvia",
    "Lebanon",
    "Lesotho",
    "Liberia",
    "Libya",
    "Liechtenstein",
    "Lithuania",
    "Luxembourg",
    "Madagascar",
    "Malawi",
    "Malaysia",
    "Maldives",
    "Mali",
    "Malta",
    "Marshall Islands",
    "Mauritania",
    "Mauritius",
    "Mexico",
    "Micronesia, Federated States of",
    "Moldova",
    "Monaco",
    "Mongolia",
    "Montenegro",
    "Morocco",
    "Mozambique",
    "Myanmar (Burma)",
    "Namibia",
    "Nauru",
    "Nepal",
    "Netherlands",
    "New Zealand",
    "Nicaragua",
    "Niger",
    "Nigeria",
    "North Macedonia",
    "Norway",
    "Oman",
    "Pakistan",
    "Palau",
    "Panama",
    "Papua New Guinea",
    "Paraguay",
    "Peru",
    "Philippines",
    "Poland",
    "Portugal",
    "Qatar",
    "Romania",
    "Russia",
    "Rwanda",
    "Saint Kitts and Nevis",
    "Saint Lucia",
    "Saint Vincent and the Grenadines",
    "Samoa",
    "San Marino",
    "Sao Tome and Principe",
    "Saudi Arabia",
    "Senegal",
    "Serbia",
    "Seychelles",
    "Sierra Leone",
    "Singapore",
    "Slovakia",
    "Slovenia",
    "Solomon Islands",
    "Somalia",
    "South Africa",
    "Spain",
    "Sri Lanka",
    "Sudan",
    "Sudan, South",
    "Suriname",
    "Sweden",
    "Switzerland",
    "Syria",
    "Taiwan",
    "Tajikistan",
    "Tanzania",
    "Thailand",
    "Togo",
    "Tonga",
    "Trinidad and Tobago",
    "Tunisia",
    "Turkey",
    "Turkmenistan",
    "Tuvalu",
    "Uganda",
    "Ukraine",
    "United Arab Emirates",
    "United Kingdom",
    "United States",
    "Uruguay",
    "Uzbekistan",
    "Vanuatu",
    "Vatican City",
    "Venezuela",
    "Vietnam",
    "Yemen",
    "Zambia",
    "Zimbabwe"
];

const disease_set = [
    "unknown",
    "other",
    "anthrax cutaneous",
    "anthrax gastrointestinous",
    "anthrax inhalation",
    "botulism",
    "brucellosis",
    "chikungunya",
    "cholera",
    "cryptococcosis",
    "cryptosporidiosis",
    "crimean-congo haemorrhagic fever",
    "dengue",
    "diphteria",
    "ebola haemorrhagic fever",
    "ehec (e.coli)",
    "enterovirus 71 infection",
    "influenza a/h5n1",
    "influenza a/h7n9",
    "influenza a/h9n2",
    "influenza a/h1n1",
    "influenza a/h1n2",
    "influenza a/h3n5",
    "influenza a/h3n2",
    "influenza a/h2n2",
    "hand, foot and mouth disease",
    "hantavirus",
    "hepatitis a",
    "hepatitis b",
    "hepatitis c",
    "hepatitis d",
    "hepatitis e",
    "histoplasmosis",
    "hiv/aids",
    "lassa fever",
    "malaria",
    "marburg virus disease",
    "measles",
    "mers-cov",
    "mumps",
    "nipah virus",
    "norovirus infection",
    "pertussis",
    "plague",
    "pneumococcus pneumonia",
    "poliomyelitis",
    "q fever",
    "rabies",
    "rift valley fever",
    "rotavirus infection",
    "rubella",
    "salmonellosis",
    "sars",
    "shigellosis",
    "smallpox",
    "staphylococcal enterotoxin b",
    "thypoid fever",
    "tuberculosis",
    "tularemia",
    "vaccinia and cowpox",
    "varicella",
    "west nile virus",
    "yellow fever",
    "yersiniosis",
    "zika",
    "legionares",
    "listeriosis",
    "monkeypox",
    "COVID-19",
    "Haemorrhagic Fever",
    "Acute Flacid Paralysis",
    "Acute gastroenteritis",
    "Acute respiratory syndrome",
    "Influenza-like illness",
    "Acute fever and rash",
    "Fever of unknown Origin",
    "Encephalitis",
    "Meningitis",
];





class SearchBar extends React.Component {
    constructor(props) {
        super(props);
        this.setArticles = props.setArticles;
        this.changeDates = this.changeDates.bind(this);
        this.changeLocation = this.changeLocation.bind(this);
        this.changeKeyTerms = this.changeKeyTerms.bind(this);
        this.submitForms = this.submitForms.bind(this);
        this.state = {
            startDate: null,
            endDate: null,
            location: "",
            key_terms: "",
        }
    }

    changeDates(inDate) {
        this.setState({startDate: inDate.startDate});
        this.setState({endDate: inDate.endDate});
    }

    changeLocation(loc) {
        this.setState({location: loc.target.value});
    }

    changeKeyTerms(kt) {
        this.setState({key_terms: kt.target.value});
    }

    submitForms() {
    
        var location = this.state.location;
        var key_terms = this.state.key_terms;

        var end_date = format(this.state.endDate, "yyyy-MM-dd");
        var start_date = format(this.state.startDate, "yyyy-MM-dd");
        
        var promiseArr = []
        var results = [];
    
        if(location === ""){
            alert("Location can not be empty");
        }else if (key_terms === ""){
            alert("Key Terms can not be empty");
        }else{
            promiseArr.push(apiFetch(end_date,start_date,key_terms,location).then((data) => {(results.push(data));}));
            Promise.all(promiseArr).then((data) => {
                var articleBoxes = [];
                for(var obj of results[0]["articles"]){
                    articleBoxes.push(new ArticleContainer(obj["article"]));
                };

                

                this.props.setArticles(articleBoxes);
            });
        }
    }

    render() {
        return (
            <div className="searchBar">
                <div class="container">
                    <div class="column">
                    <DateRangePickerComponent change={this.changeDates} dateformat='yyyy-MM-dd' id="datetimepicker" placeholder="Enter date range: "></DateRangePickerComponent>
                    </div>
                    <div class="column">
                        <form>
                            <label> 
                                <input onChange={this.changeLocation} placeholder="Location" type="text" id="location" style={{width: "370px"}}/>
                            </label>
                        </form>
                    </div>
                    <div class="column">
                    <form>
                            <label>
                                <input onChange={this.changeKeyTerms} placeholder="Key terms seperated by commas" type="text" id="keyterms" style={{width: "370px"}}/>
                            </label>
                        </form>
                    </div>
                    <button onClick={this.submitForms}>
                        Submit
                    </button>

                </div>
            </div>
        )
    }
}


export default SearchBar;