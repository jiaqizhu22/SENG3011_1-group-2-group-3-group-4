# need to scrape all countries
# 1. try return the scraped data in a format similar to data.json; 
# 2. the keys of the returned dict can be: new_cases, new_increase 
    # (the percentage of number of new cases increase in past 7 days), 
    # active_cases, active_increase, can_you_enter, what_to_expect, 
    # greenlane_agreement (*idk what this is but just chuck it in), url or 
    # link (the link to the original website for further info)
# 3. create a schema containing these attributes (keys), the table/model 
    # can be called travel or travel_info (leave it until scraping is done)

country_set = {
    "algeria", # START OF AFRICA
    "angola",
    "benin",
    "botswana",
    "burkina-faso",
    "burundi",
    "cameroon",
    "cape-verde",
    "central-african-republic",
    "chad",
    "comoros",
    "congo",
    "cote-divoire",
    "djibouti",
    "egypt",
    "equatorial-guinea",
    "eritrea",
    "ethiopia",
    "gabon",
    "gambia",
    "ghana",
    "guinea",
    "guinea-bissau",
    "kenya",
    "lesotho",
    "liberia",
    "libya",
    "madagascar",
    "malawi",
    "mali",
    "mauritania",
    "mauritius",
    "mayotte",
    "morocco",
    "mozambique",
    "namibia",
    "niger",
    "nigeria",
    "republic-of-the-congo",
    "reunion",
    "rwanda",
    "saint-helena",
    "sao-tome-and-principe",
    "senegal",
    "seychelles",
    "sierra-leone",
    "somalia",
    "south-africa",
    "south-sudan",
    "sudan",
    "swaziland",
    "tanzania",
    "togo",
    "tunisia",
    "uganda",
    "western-sahara",
    "zambia",
    "zambabwe",
    "anguilla", # START OF AMERICA
    "antigua-and-barbuda",
    "argentina",
    "aruba",
    "bahamas",
    "barbados",
    "belize",
    "bermuda",
    "bolivia",
    "brazil",
    "british-virgin-islands",
    "canada",
    "cayman-islands",
    "chile",
    "colombia",
    "costa-rica",
    "cuba",
    "dominica",
    "dominican-republic",
    "ecuador",
    "el-salvador",
    "falkland-islands",
    "french-guiana",
    "greenland",
    "grenada",
    "guadeloupe",
    "guatemala",
    "guyana",
    "haiti",
    "honduras",
    "jamaica",
    "martinique",
    "mexico",
    "montserrat",
    "netherlands-antilles",
    "nicaragua",
    "panama",
    "paraguauy",
    "peru",
    "puerto-rico",
    "saint-kitts-and-nevis",
    "saint-lucia",
    "saint-pierre-and-miquelon",
    "saint-vincent-and-grenadines",
    "saint-barthelemy",
    "saint-martin",
    "suriname",
    "trinidad-and-tobago",
    "turks-and-caicos-islands",
    "united-states",
    "uruguay",
    "us-minor-outlying-islands",
    "venezuela",
    "virgin-islands",
    "antarctica", # START OF ANTARCTICA
    "bouvet-island",
    "french-southern-territories",
    "heard-and-mcdonald-islands",
    "south-georgia-and-the-sandwich-islands",
    "afghanistan", # START OF ASIA
    "bahrain",
    "bangladesh",
    "bhutan",
    "british-indian-ocean-territory",
    "brunei-darussalam",
    "cambodia",
    "china",
    "christmas-island",
    "hong-kong",
    "india",
    "iran",
    "iraq",
    "israel",
    "japan",
    "jordan",
    "kazakhstan",
    "kuwait",
    "kyrgyzstan",
    "laos",
    "lebanon",
    "macao",
    "maldives",
    "mongolia",
    "myanmar",
    "nepal",
    "north-korea",
    "oman",
    "pakistan",
    "palestine",
    "south-korea",
    "sri-lanka",
    "syria",
    "taiwan",
    "tajikistan",
    "timor-leste",
    "turkmenistan",
    "uzbekistan",
    "yemen",
    "ala-aland-islands", # START OF EUROPE
    "albania",
    "andorra",
    "armenia",
    "austria",
    "azerbaijan",
    "belarus",
    "belgium",
    "bosnia-and-herzegovina",
    "bulgaria",
    "croatia",
    "cyprus",
    "czech-republic",
    "denmark",
    "estonia",
    "faroe-islands",
    "finland",
    "france",
    "georgia",
    "germany",
    "gibraltar",
    "greece",
    "guernsey",
    "hungary",
    "iceland",
    "ireland",
    "isle-of-man",
    "italy",
    "jersey",
    "kosovo",
    "latvia",
    "liechtenstein",
    "lithuania",
    "luxembourg",
    "malta",
    "moldova",
    "monaco",
    "montenegro",
    "netherlands",
    "north-macedonia",
    "norway",
    "poland",
    "portugal",
    "romania",
    "russia",
    "san-marino",
    "serbia",
    "slovakia",
    "slovenia",
    "spain",
    "svalbard-and-jan-mayen-islands",
    "sweden",
    "switzerland",
    "ukraine",
    "united-kingdom",
    "vatican-city",
    "qatar", # START OF MIDDLE-EAST
    "saudi-arabia",
    "turkey",
    "united-arab-emirates",
    "american-samoa", # START OF OCEANA
    "australia",
    "cocos-islands",
    "cook-islands",
    "fiji",
    "french-polynesia",
    "guam",
    "kiribati",
    "marshall-islands",
    "micronesia",
    "nauru",
    "new-caledonia",
    "new-zealand",
    "niue",
    "norfolk-island",
    "northern-mariana-islands",
    "palau",
    "papua-new-guinea",
    "pitcairn",
    "samoa",
    "solomon-islands",
    "tokelau",
    "tonga",
    "tuvalu",
    "vanuatu",
    "wallis-and-futuna-islands",
    "indonesia", # START OF SEA
    "malaysia",
    "philippines",
    "singapore",
    "thailand",
    "vietnam"
}

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from time import strptime
import calendar

countries_list = []
for country in country_set:
    counter = 0
    URL = "https://trutrip.co/country/"+country
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    new_cases = soup.find("", {"": ""})
    new_increase = soup.find("", {"": ""})
    active_cases = soup.find("", {"": ""})
    active_increase = soup.find("", {"": ""})

    can_you_enter = soup.find_all("", {"": ""})

    # Access the 'what to expect' section
    expectation_titles = soup.find_all("", {"": ""})
    for ind, title in enumerate(expectation_titles):
        splitTitle = re.split('>|<',str(title))



    # Dictionary for expectations section
    what_to_expect = {
        "before_your_trip": before_your_trip,
        "on_arrival": on_arrival,
        "quarantine_details": quarantine_details,
        "travel_restrictions": travel_restrictions
    }

    # lists the countries under any lane agreements with this country
    # null if no countries under this lane at this time
    lanes = {
        "green": [green],
        "yellow": [yellow],
        "red": [red]
    }

    article = { #making dict of the info.
        "country": country, # country name
        "new_cases": new_cases, # Number of new cases last 7 days
        "new_increase": new_increase, # The % new increases in past 7 days
        "active_cases": active_cases, 
        "active_increase":active_increase, 
        "can_you_enter": can_you_enter, # text
        "what_to_expect": what_to_expect, # contains what_to_expect dictionary
        "lanes": lanes,
        "link": link,
    }

    countries_list.append(article) #appending the dicts into the list
    if len(article) == 0: #stops the loop when it reaches the end
        break

#print(countries_list) #debug

df = pd.DataFrame(countries_list)

#print(df) #pandas dataframe

with open('trudata.json', 'w') as f:
    json.dump(countries_list, f)

print("COMPLETE")
