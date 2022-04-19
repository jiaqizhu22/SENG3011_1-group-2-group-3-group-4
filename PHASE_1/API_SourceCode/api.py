# This file is used to directly load data from data.json into db.sqlite3.
# This file contains a draft function that can be used in view.py "/Search"
# endpoint for fetching at every request.

# Settings: required module for TIMEZONE
from imghdr import what
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

import django
django.setup()

import json
from scraper.models import *
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
                         
    with open('./scraper/trudata.json', 'r') as json_file:
        # Store the json data as a list
        data = json.load(json_file)
        
        for travelInfo in data:
            
            # Create travel info
            try:
                travelInfoObj = TravelInfo.objects.get(country = travelInfo['country'])
            except ObjectDoesNotExist:
                travelInfoObj = TravelInfo.objects.create(
                    country = travelInfo['country'],
                    new_cases = travelInfo['new_cases'],
                    active_cases = travelInfo['active_cases'],
                    new_percentage = travelInfo['new_increase'],
                    active_percentage = travelInfo['active_increase'],
                    can_you_enter = travelInfo['can_you_enter']
                )
                
            # Create overview
            overview = travelInfo['overview']
            try:
                overviewObj = Overview.objects.get(travel_id = travelInfoObj)
                overviewObj.open_status = overview['open_status']
                overviewObj.quarantine_days = overview['quarentine_days']
                overviewObj.save()
            except ObjectDoesNotExist:
                overviewObj = Overview.objects.create(
                    travel_id = travelInfoObj,
                    open_status = overview['open_status'],
                    quarantine_days = overview['quarentine_days']
                )
                
            travelInfoObj.overview = overviewObj
            travelInfoObj.save()
                
            # Create what to expect
            wte = travelInfo['what_to_expect']
            try:
                wteObj = WhatToExpect.objects.get(travel_id = travelInfoObj)
                wteObj.before_your_trip = wte['before_your_trip']
                wteObj.on_arrival = wte['on_arrival']
                wteObj.quarantine_details = wte['quarantine_details']
                wteObj.travel_restrictions = wte['travel_restrictions']
                wteObj.save()
            except ObjectDoesNotExist:
                wteObj = WhatToExpect.objects.create(
                    travel_id = travelInfoObj,
                    before_your_trip = wte['before_your_trip'],
                    on_arrival = wte['on_arrival'],
                    quarantine_details = wte['quarantine_details'],
                    travel_restrictions = wte['travel_restrictions']
                )
                
            travelInfoObj.what_to_expect = wteObj
            travelInfoObj.save()
            
            # No lanes in scraper as of right now
                
            
    print('COMPLETE LOADING DATA')
            
            
            
            