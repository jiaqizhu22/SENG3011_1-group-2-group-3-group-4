from datetime import date
import json
import re
from articles import Articles
from diseases import Diseases
from locations import Locations
from places import Places
from reports import Reports
from syndromes import Syndromes
from report_diseases import Report_diseases
from report_syndromes import Report_syndromes

articles_list = []
article_id = 0

reports_list = []
report_id = 0

# diseases_list = []
# syndrome_id = 0
# locations_list = []
# location_id = 0
# places_list = []

# syndromes_list = []
# report_diseases_list = []
# report_syndromes_list = []
i = 0
with open('data.json', 'r') as json_file:
    # Store the json data as a list
    data = json.load(json_file)
    for article in data:
        article_id += 1
        
        url = article['url']
        date_of_publication = article['date_of_publication']
        headline = article['headline']
        main_text = article['main_text']
        report = article['reports']
        for items in report:
            report_id += 1
            diseases = report['diseases']
            event_date = report['event_date']
        Report = Reports(article_id, report_id, event_date)
        reports_list.append(Report)
        Article = Articles(article_id,url,date_of_publication,headline,main_text)
        articles_list.append(Article)

for article in articles_list:
    print(article.headline)