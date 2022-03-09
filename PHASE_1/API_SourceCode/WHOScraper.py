#IF required we can add the entire body section of the thing into the dictionary but for now it just has those 4 fields
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

lstBasicInfo = []
for pageNum in range(0,150): #change this for the amount of pages to check. if its over the number of pages itll end auto. If you wanna check for example, page 7, do range(7,8)
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
        location = dl[1].strip()
        disease = dl[0].strip()
        date = splited[8][:-3]
        url = str(outbreakLink[c]).split("\"")[3]
        currentPage = BeautifulSoup(requests.get(url).content, "html.parser")
        if len(disease) == 4 and disease.isnumeric(): #if the entry is using the old schema, then do this to get the disease
            disease1 = re.split('>|<',str(str(currentPage.find_all("li", {"class": "active"}))))[16]
            disease2 = re.split('- |– | ｰ|in ',str(disease1))
            disease = disease2[0] 

        BasicInfoDict = { #making dict of the info. 
          "date": date,
          "disease": disease,
          "location": location,
          "URL":url,
        }
        lstBasicInfo.append(BasicInfoDict) #appending the dicts into the list
        if len(BasicInfoDict) == 0: #stops the loop when it reaches the end
            break

#print(lstBasicInfo) #debug

df = pd.DataFrame(lstBasicInfo)

print(df) #pandas dataframe
