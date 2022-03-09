import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
import os

#url = "https://www.who.int/emergencies/disease-outbreak-news"

def get_outbreak_news(url): 

    headers = {}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    print(soup.prettify())

    name = soup.select_all(selector=".full-title").get_text()
    name = name.strip() # removes white spaces
    # Test
    print(name)
    date, title = name.split('|') #does this split the date and title with '|' delimiter?

    return date, title

# func to return all the text in article
def get_article_text(url):

    headers = {}

    r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")
    print(soup.prettify())

    # Work out how to access each text section... if we cant do it this way then grab all of it and we can split the text
    background = soup.select_all(selector=".sf-accordion_title").get_text().strip()
    #response = soup.select_all(selector=".full-title").get_text().strip()
    #risk_assessment = soup.select_all(selector=".full-title").get_text().strip()
    #advice = soup.select_all(selector=".full-title").get_text().strip()

    return background #response, risk_assessment, advice