import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import json
from scraper.models import Articles, Locations, Reports
from django.utils.dateparse import parse_datetime
from django.conf import settings
from django.utils.timezone import make_aware
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


if __name__ == '__main__': 
    with open('./scraper/data.json', 'r') as json_file:
        # Store the json data as a list
        data = json.load(json_file)
        
        for article in data:
            settings.TIME_ZONE
            new_date = make_aware(parse_datetime(article['date_of_publication']))
            new_article_obj = Articles.objects.create(
                url=article['url'],
                date_of_publication=new_date,
                headline=article['headline'],
                main_text=article['main_text']
            )
                
            report_list = article['reports']
            #print(report_list)
            # for report in report_list:
            disease = ''
            if report_list['diseases'] != []:
                disease = report_list['diseases'][0]
            syndrome = ''
            if report_list['syndromes'] != []:
                syndrome = report_list['syndromes'][0]
            date = None
            if report_list['event_date'] != [] == report_list['event_date'] != '':
                date = make_aware(parse_datetime(report_list['event_date']))                
            
            new_report = Reports.objects.create(
                parent_id=new_article_obj,
                diseases=disease,
                syndromes=syndrome,
                event_date=date
            )
            
            if report_list['locations'] != []:
                try:
                    locations = Locations.objects.get(country=report_list['locations'][0]['country'], location=report_list['locations'][0]['location'])
                    print(locations)
              
                    new_report.locations.add(locations)
                    
                except ObjectDoesNotExist:
                    location = Locations.objects.create(
                        country=report_list['locations'][0]['country'],
                        location=report_list['locations'][0]['location']
                    )
                    new_report.locations.add(location)
                #except MultipleObjectsReturned:
                    
                
        
    print('COMPLETE LOADING DATA')
            
            
            
            