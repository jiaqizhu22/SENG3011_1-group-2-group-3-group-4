import React from 'react';
import './searchBar.css';
import {useState} from 'react'
import { DateRangePickerComponent } from '@syncfusion/ej2-react-calendars';
import apiFetch from '../../index.js';




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
  "Zimbabwe"]

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
]




function submitForms(){

  var dates = String(document.getElementById('datetimepicker').value);

  var location = document.getElementById('location').value;
  var key_terms = document.getElementById('keyterms').value;
  var end_date = dates.split(" - ")[1];
  var start_date = dates.split(" - ")[0];
  
  var promiseArr = []
  var results = [];
  //alert(location.value + keyTerms.value + dates.value);
  if(location === ""){
    alert("Location can not be empty");
    //for (var country of country_list){
    //  promiseArr.push(apiFetch(end_date,start_date,key_terms,country).then((data) => {(results.push(data));}));
    //}
  }else if (key_terms === ""){
    alert("Key Terms can not be empty");
    //for (var disease of disease_set){
    //  promiseArr.push(apiFetch(end_date,start_date,disease,location).then((data) => {(results.push(data));}));
    //}
  }else{
    promiseArr.push(apiFetch(end_date,start_date,key_terms,location).then((data) => {(results.push(data));}));
    Promise.all(promiseArr).then((data) => {
      var theDiv = document.getElementById("crap");

      for(var obj of results[0]["articles"]){
        theDiv.innerHTML += "<br />";
        theDiv.innerHTML += "--------------------------------";
        theDiv.innerHTML += "<br />";
        theDiv.innerHTML += JSON.stringify(obj); //replace with nice looking component
        theDiv.innerHTML += "<br />";
        theDiv.innerHTML += "--------------------------------";
        theDiv.innerHTML += "<br />";
      }

      
      
      (console.log(results));
    
    
    
    
    
    });
  }

  

  //console.log(results)
  
}



const SearchBar = () => (
    <div className="searchBar">
      <div class="container">
        <div class="column">
        <DateRangePickerComponent format='yyyy-MM-dd' id="datetimepicker" placeholder="Enter date range: "></DateRangePickerComponent>
        </div>
        <div class="column">
          <form>
            <label> 
              <input placeholder="Location" type="text" id="location" style={{width: "370px"}}/>
            </label>
          </form>
        </div>
        <div class="column">
        <form>
            <label>
              <input placeholder="Key terms seperated by commas" type="text" id="keyterms" style={{width: "370px"}}/>
            </label>
          </form>
        </div>
        <button onClick={submitForms}>
          Submit
        </button>

      </div>
      
    </div>
  )
export default SearchBar;