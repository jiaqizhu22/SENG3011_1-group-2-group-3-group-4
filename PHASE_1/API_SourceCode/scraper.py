disease_set = {
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
}


syndrome_set = {
    "Haemorrhagic Fever",
    "Acute Flacid Paralysis",
    "Acute gastroenteritis",
    "Acute respiratory syndrome",
    "Influenza-like illness",
    "Acute fever and rash",
    "Fever of unknown Origin",
    "Encephalitis",
    "Meningitis",
}



months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


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
    if(year.isdigit() and month.isdigit() and day.isdigit() and len(year) == 4 and len(day) <=  2):
        return (year+"-"+month+"-"+day)
    return False


lstBasicInfo = []
for pageNum in range(0,150): #change this for the amount of pages to check. if its over the number of pages itll end auto. If you wanna check for example, page 7, do range(7,8)
    counter = 0
    URL = "https://www.who.int/emergencies/disease-outbreak-news/"+str(pageNum) #iterates over the pages
    print(URL)
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    outbreakTitles = soup.find_all("h4", {"class": "sf-list-vertical__title"}) #title and info
    outbreakLinks = soup.find_all("a", {"class": "sf-list-vertical__item"}) #link

    for ind, title in enumerate(outbreakTitles): #loop between the info
        splitTitle = re.split('>|<',str(title))
        diseaseAndLocation = re.split('- |– |ｰ ',str(splitTitle[4]))

        illness = diseaseAndLocation[0].strip()
        date = splitTitle[8][:-3]
        date = dateConverter(date)
        url = str(outbreakLinks[ind]).split("\"")[3]
        diseases = []
        syndromes = []
        eventDate = date
        
        currentPage = BeautifulSoup(requests.get(url).content, "html.parser")
        if len(illness) == 4 and illness.isnumeric(): #if the entry is using the old schema, then do this to get the disease
            #print(re.split('>|<',str(str(currentPage.find_all("li", {"class": "active"})))))
            illness1 = re.split('>|<',str(str(currentPage.find_all("li", {"class": "active"}))))[16]
            illness2 = re.split('- |– |ｰ | in',str(illness1))
            illness = illness2[0]
            if illness[-1] == ' ':
                illness = illness[:-1]
            if len(illness) == 4 and illness.isnumeric():
               illness = illness2[1] 

        try:
            country = diseaseAndLocation[1].strip()
        except:
            t1 = re.split('>|<',str(str(currentPage.find_all("li", {"class": "active"}))))[16]
            t2 = re.split('- |– |ｰ | in|',str(t1))
            try:
                country = t2[1]
            except:
                country = ""

        main_text = ""
        for para in currentPage.find_all("p"):
            main_text = main_text + (para.get_text().strip())


        # Check if illness is a syndrome or a disease
        isSyndrome = False
        isDisease = False
        for syndrome in syndrome_set:
            curSyndromeCheck = syndrome.lower()
            if curSyndromeCheck in illness.lower() or illness.lower() in curSyndromeCheck or curSyndromeCheck in main_text:
                #syndromes.append(illness.strip())
                syndromes.append(syndrome)
                isSyndrome = True
                
                
        for disease in disease_set:
            curDiseaseCheck = disease.lower()
            if curDiseaseCheck in illness.lower() or illness.lower() in curDiseaseCheck or curDiseaseCheck in main_text:
                #syndromes.append(illness.strip())
                diseases.append(disease)
                isDisease = True
                
                
        if isSyndrome is False and isDisease is False and "update" not in illness.lower(): # For now, any unrecognised illness is a disease. This may not be to spec.
            diseases.append(illness.strip())



        headline = currentPage.find("h1").get_text().strip()


        indices = [i for i, x in enumerate(re.split(' |,',str(main_text))) if x in months]
        #here we will need to collect all valid datess and make a date range out of them for the event date. For now it
        #is sonly doing one date 
        for i in indices:
            textList = re.split(' |,',str(main_text))
           # print(textList[i-1] + " " + textList[i]+ " " +textList[i+1].replace(".",""))
            if(dateConverter(textList[i-1] + " " + textList[i]+ " " +textList[i+1].replace(".",""))):
                eventDate = dateConverter(textList[i-1] + " " + textList[i]+ " " +textList[i+1].replace(".",""))
                #print(eventDate)
                break
            
        
        #main_text = currentPage.find_all("article", {"class": "sf-detail-body-wrapper"})
        locs_list = []
        for country in  re.split(', |and ',str(country)):
            loc_object = {
                "country": country,
                "location":"",   #this needs to be sorted out
            }
            locs_list.append(loc_object)

        report = {
            "diseases": diseases,
            "syndromes": syndromes,
            "event_date":eventDate, #this needs to be sorted out. Right now it is just getting the first date that isnt the publishing date and using that as the event date
            "locations":locs_list,  
        }

            
        article = { #making dict of the info.
            "url":url,
            "date_of_publication": date,
            "headline": headline,
            "main_text":main_text,
            "reports":[report],
        }
        lstBasicInfo.append(article) #appending the dicts into the list
        if len(article) == 0: #stops the loop when it reaches the end
            break

        with open('data.json', 'w') as f:
            json.dump(lstBasicInfo, f, indent=2)

        #print(json.dumps(article, indent=2)) #pretty print json to look at

       # print()

#print(lstBasicInfo) #debug

df = pd.DataFrame(lstBasicInfo)

#print(df) #pandas dataframe

with open('data.json', 'w') as f:
    json.dump(lstBasicInfo, f)

print("COMPLETE")
