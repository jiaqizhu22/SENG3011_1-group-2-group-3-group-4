# need to scrape all countries
# 1. try return the scraped data in a format similar to data.json; 
# 2. the keys of the returned dict can be: new_cases, new_increase 
    # (the percentage of number of new cases increase in past 7 days), 
    # active_cases, active_increase, can_you_enter, what_to_expect, 
    # greenlane_agreement (*idk what this is but just chuck it in), url or 
    # link (the link to the original website for further info)
# 3. create a schema containing these attributes (keys), the table/model 
    # can be called travel or travel_info (leave it until scraping is done)

import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from time import strptime
import calendar

# Dictionary for expectations section
what_to_expect = {
    "vaccine_exemptions": vaccine_exemptions,
    "forms": forms,
    "testing_requirements": testing_requirements,
    "quarantine_requirements": quarantine_requirements,
    "country_specific_restrictions": country_specific_restrictions
}

# lists the countries under any lane agreements with this country
# null if no countries under this lane at this time
lanes = {
    "green": [green],
    "yellow": [yellow],
    "red": [red]
}

article = { #making dict of the info.
    "url": url, # url of this page
    "country": country, # country name
    "new_cases": new_cases, # Number of new cases last 7 days
    "new_increase": new_increase, # The % new increases in past 7 days
    "active_cases": active_cases, # null if not displayed bcs total is shown
    "active_increase":active_increase, # null if not displayed
    "total_cases": total_cases, # null if not displayed bcs active is shown
    "can_you_enter": can_you_enter, # text
    "what_to_expect": what_to_expect, # List of expectations
    "lanes": lanes,
    "other_important_info": other_important_info,
    "link": link,
}