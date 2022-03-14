disease_list = [
{ "name": "unknown" },
{ "name": "other" },
{ "name": "anthrax cutaneous" },
{ "name": "anthrax gastrointestinous" },
{ "name": "anthrax inhalation" },
{ "name": "botulism" },
{ "name": "brucellosis" },
{ "name": "chikungunya" },
{ "name": "cholera" },
{ "name": "cryptococcosis" },
{ "name": "cryptosporidiosis" },
{ "name": "crimean-congo haemorrhagic fever" },
{ "name": "dengue" },
{ "name": "diphteria" },
{ "name": "ebola haemorrhagic fever" },
{ "name": "ehec (e.coli)" },
{ "name": "enterovirus 71 infection" },
{ "name": "influenza a/h5n1" },
{ "name": "influenza a/h7n9" },
{ "name": "influenza a/h9n2" },
{ "name": "influenza a/h1n1" },
{ "name": "influenza a/h1n2" },
{ "name": "influenza a/h3n5" },
{ "name": "influenza a/h3n2" },
{ "name": "influenza a/h2n2" },
{ "name": "hand, foot and mouth disease" },
{ "name": "hantavirus" },
{ "name": "hepatitis a" },
{ "name": "hepatitis b" },
{ "name": "hepatitis c" },
{ "name": "hepatitis d" },
{ "name": "hepatitis e" },
{ "name": "histoplasmosis" },
{ "name": "hiv/aids" },
{ "name": "lassa fever" },
{ "name": "malaria" },
{ "name": "marburg virus disease" },
{ "name": "measles" },
{ "name": "mers-cov" },
{ "name": "mumps" },
{ "name": "nipah virus" },
{ "name": "norovirus infection" },
{ "name": "pertussis" },
{ "name": "plague" },
{ "name": "pneumococcus pneumonia" },
{ "name": "poliomyelitis" },
{ "name": "q fever" },
{ "name": "rabies" },
{ "name": "rift valley fever" },
{ "name": "rotavirus infection" },
{ "name": "rubella" },
{ "name": "salmonellosis" },
{ "name": "sars" },
{ "name": "shigellosis" },
{ "name": "smallpox" },
{ "name": "staphylococcal enterotoxin b" },
{ "name": "thypoid fever" },
{ "name": "tuberculosis" },
{ "name": "tularemia" },
{ "name": "vaccinia and cowpox" },
{ "name": "varicella" },
{ "name": "west nile virus" },
{ "name": "yellow fever" },
{ "name": "yersiniosis" },
{ "name": "zika" },
{ "name": "legionares" },
{ "name": "listeriosis" },
{ "name": "monkeypox" },
{ "name": "COVID-19" }
]


syndrome_list = [
{ "name": "Haemorrhagic Fever" },
{ "name": "Acute Flacid Paralysis" },
{ "name": "Acute gastroenteritis" },
{ "name": "Acute respiratory syndrome" },
{ "name": "Influenza-like illness" },
{ "name": "Acute fever and rash" },
{ "name": "Fever of unknown Origin" },
{ "name": "Encephalitis" },
{ "name": "Meningitis" },
]


#IF required we can add the entire body section of the thing into the dictionary but for now it just has those 4 fields
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from time import strptime
import calendar


def dateConverter(date):
    date = date.split(" ")
    year = date[2]
    month = str(list(calendar.month_name).index(date[1])).zfill(2)
    day = date[0].zfill(2)
    return (year+"-"+month+"-"+day) 


lstBasicInfo = []
<<<<<<< HEAD
for pageNum in range(0,10): #change this for the amount of pages to check. if its over the number of pages itll end auto. If you wanna check for example, page 7, do range(7,8)
=======
for pageNum in range(12,13): #change this for the amount of pages to check. if its over the number of pages itll end auto. If you wanna check for example, page 7, do range(7,8)
>>>>>>> main
    counter = 0
    URL = "https://www.who.int/emergencies/disease-outbreak-news/"+str(pageNum) #iterates over the pages
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    outbreakTitle = soup.find_all("h4", {"class": "sf-list-vertical__title"}) #title and info
    outbreakLink = soup.find_all("a", {"class": "sf-list-vertical__item"}) #link

    for c, i in enumerate(outbreakTitle): #loop between the info
        splited = re.split('>|<',str(i))
        dl = re.split('- |– | ｰ',str(splited[4]))
<<<<<<< HEAD
        if (dl[1]):
            location = dl[1].strip()
        else:
            location = ""
=======

            
>>>>>>> main
        illness = dl[0].strip()
        date = splited[8][:-3]
        date = dateConverter(date)
        url = str(outbreakLink[c]).split("\"")[3]
        diseases = []
        syndromes = []
        
        currentPage = BeautifulSoup(requests.get(url).content, "html.parser")
        if len(illness) == 4 and illness.isnumeric(): #if the entry is using the old schema, then do this to get the disease
            illness1 = re.split('>|<',str(str(currentPage.find_all("li", {"class": "active"}))))[16]
            illness2 = re.split('- |– | ｰ|in ',str(illness1))
            illness = illness2[0] 

        try:
            country = dl[1].strip()
        except:
            t1 = re.split('>|<',str(str(currentPage.find_all("li", {"class": "active"}))))[16]
            t2 = re.split('- |– | ｰ|in ',str(t1))
            country = t2[1] 

        #checking is illness is disease or syndrome
        check = 0
        for syndrome in syndrome_list:
            curSyndromeCheck = list(syndrome.values())[0].lower()
            if curSyndromeCheck in illness.lower() or illness.lower() in curSyndromeCheck:
                syndromes.append(illness)
                check = check + 1
        if check == 0:
            for disease in disease_list:
                curDiseaseCheck = list(disease.values())[0].lower()
                if curDiseaseCheck in illness.lower() or illness.lower() in curDiseaseCheck:
                    diseases.append(illness)
                    check = check + 1
        if check == 0:  #appending any unrecognised illness into the diseases list. Im not ssure if this is to spec. But sometimes there are illnesses not included in the json that they gave us
            diseases.append(illness)



        headline = currentPage.find("h1").get_text().strip()
        main_text = ""
        for para in currentPage.find_all("p"):
            main_text = main_text + (para.get_text().strip())


        #main_text = currentPage.find_all("article", {"class": "sf-detail-body-wrapper"})
        locs_list = []
        for country in  re.split(', |and ',str(country)):
            loc_object = {
<<<<<<< HEAD
                "country": location,
=======
                "country": country,
>>>>>>> main
                "location":"",   #this needs to be sorted out
            }
            locs_list.append(loc_object)

        report = {
            "diseases": diseases,
            "syndromes": syndromes,
            "event_date":"", #this needs to be sorted out
            "locations":locs_list,  
        }

            
        article = { #making dict of the info.
            "url":url,
            "date_of_publication": date,
            "headline": headline,
            "main_text":main_text,
            "reports":report,
        }
        lstBasicInfo.append(article) #appending the dicts into the list
        if len(article) == 0: #stops the loop when it reaches the end
            break

        with open('data.json', 'w') as f:
            json.dump(lstBasicInfo, f)

<<<<<<< HEAD
        #print(json.dumps(article, indent=2)) #pretty print json to look at
=======
        print(json.dumps(article, indent=2)) #pretty print json to look at
>>>>>>> main

        
        #print()

#print(lstBasicInfo) #debug

df = pd.DataFrame(lstBasicInfo)

#print(df) #pandas dataframe
