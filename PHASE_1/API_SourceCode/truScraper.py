# need to scrape all countries
# 1. try return the scraped data in a format similar to data.json; 
# 2. the keys of the returned dict can be: new_cases, new_increase 
    # (the percentage of number of new cases increase in past 7 days), 
    # active_cases, active_increase, can_you_enter, what_to_expect, 
    # greenlane_agreement (*idk what this is but just chuck it in), url or 
    # link (the link to the original website for further info)
# 3. create a schema containing these attributes (keys), the table/model 
    # can be called travel or travel_info (leave it until scraping is done)

country_set = [
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
    "congo-kinshasa",
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
    "congo-brazzaville",
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
    "zimbabwe",
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
    "falkland-islands-malvinas",
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
    "paraguay",
    "peru",
    "puerto-rico",
    "saint-kitts-and-nevis",
    "saint-lucia",
    "saint-pierre-and-miquelon",
    "saint-vincent-and-the-grenadines",
    "saint-barthelemy",
    "saint-martin-french-part",
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
    "south-georgia-and-the-south-sandwich-islands",
    "afghanistan", # START OF ASIA
    "bahrain",
    "bangladesh",
    "bhutan",
    "british-indian-ocean-territory",
    "brunei",
    "cambodia",
    "china",
    "christmas-island",
    "hong-kong-sar-china",
    "india",
    "iran",
    "iraq",
    "israel",
    "japan",
    "jordan",
    "kazakhstan",
    "kuwait",
    "kyrgyzstan",
    "lao-pdr",
    "lebanon",
    "macao-sar-china",
    "maldives",
    "mongolia",
    "myanmar",
    "nepal",
    "korea-north",
    "oman",
    "pakistan",
    "palestine",
    "korea-south",
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
    "macedonia",
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
    "holy-see-vatican-city-state",
    "qatar", # START OF MIDDLE-EAST
    "saudi-arabia",
    "turkey",
    "united-arab-emirates",
    "american-samoa", # START OF OCEANA
    "australia",
    "cocos-keeling-islands",
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
]

tempSet = ["australia","chambodia","india","malaysia","jumbotown","thailand"] # testing

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from time import strptime
import calendar

countries_list = []
counter = 0
for country in country_set:
    counter = counter + 1
    print(counter)
    print(country)
    URL = "https://trutrip.co/country/"+country
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    errorCheck = len(soup.find_all("div", {"class": "result-error-message"}))
    if errorCheck != 0:
        print("skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped skipped ")
        pass
    else:
        print("done")

        cases_scrape = soup.find_all("div", {"class": "h5 font-weight-bold"})
        casesIncrease_scrape = soup.find_all("span", {"class": "align-middle"})
        new_cases = re.split('<|>',str(cases_scrape[1]))[2]
        new_increase = re.split('<|>',str(casesIncrease_scrape[0]))[2]
        active_cases = re.split('<|>',str(cases_scrape[2]))[2]
        active_increase = re.split('<|>',str(casesIncrease_scrape[1]))[2]
        can_you_enter = ' '.join(soup.find("div", {"class": "mb-5"}).stripped_strings).split("Can you enter? ")[1]

        # Access the 'what to expect' section
        expectation_titles = soup.find_all("p", {"class": "font-weight-bold mb-0"})
        for ind, title in enumerate(expectation_titles):
            splitTitle = re.split('>|<',str(title))[2]
        bodyText = ' '.join(soup.find("div", {"class": "col-12 col-md-10 col-lg-9"}).stripped_strings)
        bodyText = re.split('Can you enter? |📝 Before your trip |🛬 On Arrival |😷 Quarantine details |🛂 Travel restrictions',bodyText)
        before_your_trip = bodyText[1]
        on_arrival = bodyText[2]
        quarantine_details = bodyText[3]
        travel_restrictions = bodyText[4]
        # Dictionary for expectations section
        what_to_expect = {
            "before_your_trip": before_your_trip,
            "on_arrival": on_arrival,
            "quarantine_details": quarantine_details,
            "travel_restrictions": travel_restrictions
        }

        # lists the countries under any lane agreements with this country
        # null if no countries under this lane at this time
        greenLanes = ','.join(soup.find("div", {"class": "text-body2"}).stripped_strings).split(",")
        overviewData = ', '.join(soup.find("ul", {"class": "list-type-custom text-body2 mb-3"}).stripped_strings).split(", ")
        openStatus = overviewData[0]
        quarentineDays = overviewData[1]
        overview = {
        "open_status": openStatus,
        "quarentine_days": quarentineDays,
        }

        article = { #making dict of the info.
            "country": country, # country name
            "overview": overview, # open status and quarantine days
            "new_cases": new_cases, # Number of new cases last 7 days
            "new_increase": new_increase, # The % new increases in past 7 days
            "active_cases": active_cases, 
            "active_increase":active_increase, 
            "can_you_enter": can_you_enter, # text
            "what_to_expect": what_to_expect, # contains what_to_expect dictionary
            "greenLanes": greenLanes,
            "link": URL,
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
