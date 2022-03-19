# This file is used to directly load data from data.json into db.sqlite3.
# This file contains a draft function that can be used in view.py "/Search"
# endpoint for fetching at every request.

# Settings: required module for TIMEZONE
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
        
        # Loop through article_list and create db objects
        for article in data:
            # Set up timezone
            settings.TIME_ZONE
            # Make parsed date aware of timezone
            new_date = make_aware(parse_datetime(article['date_of_publication']))
            
            # create Article model
            try:
                new_article_obj = Articles.objects.get(url=article['url'])
                print("Article exists: ", new_article_obj._id)
            except ObjectDoesNotExist:
                new_article_obj = Articles.objects.create(
                    url=article['url'],
                    date_of_publication=new_date,
                    headline=article['headline'],
                    main_text=article['main_text']
                )
                print('New article created: ', new_article_obj._id)
                
            # Create a list of reports in the article
            report_list = article['reports']
            
            # Even though currently each report_list only contains one report
            # Loop through report_list to create Report model
            # Assume there is no duplicate for any report in the db
            for report in report_list:
                # Assume only one disease/syndrome in the report
                disease = None
                if report['diseases'] != []:
                    disease = report['diseases'][0]
                syndrome = None
                if report['syndromes'] != []:
                    syndrome = report['syndromes'][0]
                event_date = None
                # print(report['event_date'])
                if report['event_date'] != "":
                    event_date = make_aware(parse_datetime(report['event_date']))                
                
                try:
                    new_report = Reports.objects.get(event_date=event_date, diseases=disease, syndromes=syndrome)
                    print('Report exists: ', new_report.id)
                except ObjectDoesNotExist:
                    new_report = Reports.objects.create(
                        parent_id=new_article_obj,
                        diseases=disease,
                        syndromes=syndrome,
                        event_date=event_date
                    )
                    print('New report created: ', new_report.id)              

                # Check if report contains location
                # Assume only 1 location is in report
                if report['locations'] != []:
                    # Check if the location already exists in db
                    try:
                        the_location = Locations.objects.get(country=report['locations'][0]['country'], location=report['locations'][0]['location'])
                        # Assign foreign key to new_report obj
                        new_report.locations = the_location
                        new_report.save()
                        print('Location exists and added: ')
                        
                    except ObjectDoesNotExist:
                        # Create new location obj
                        the_location = Locations.objects.create(
                            country=report['locations'][0]['country'],
                            location=report['locations'][0]['location']
                        )
                        new_report.locations = the_location
                        new_report.save()
                        print('New location created and added: ')
                        
                    # If Locations.objects.get() return multiple objs
                    # We need to add an exception:
                    # except MultipleObjectsReturned:
                         
    print('COMPLETE LOADING DATA')
            
            
            
            