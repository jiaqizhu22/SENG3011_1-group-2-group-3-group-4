from django.db import models
from datetime import datetime


class Articles(models.Model):
    _id = models.AutoField(db_column='_id', primary_key=True)
    url = models.URLField(db_column='url')
    date_of_publication = models.DateTimeField(db_column='date_of_publication')
    headline = models.CharField(db_column='headline', max_length=100)
    main_text = models.TextField(db_column='main_text')
    
    # Stringfy article info
    '''
    def __str__(self):
        return {
            'url': self.url,
            'date_of_publication': self.date_of_publication.strftime("%Y-%m-%dT%H-%M-%S"),
            'headline': self.headline,
            'main_text': self.main_text,
        }
    ''' 
    
    
class Locations(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    country = models.CharField(db_column='country', max_length=50, blank=True)
    location = models.CharField(db_column='location', max_length=50, blank=True)
    
    # Stringfy location
    def __str__(self):
        return {
            'country': self.country,
            'location': self.location
        }
    

class Reports(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    parent_id = models.ForeignKey(Articles, on_delete=models.CASCADE)
    event_date = models.DateTimeField(db_column='event_date', blank=True, null=True)
    diseases = models.CharField(db_column='diseases', max_length=50, blank=True, null=True)
    syndromes = models.CharField(db_column='syndromes', max_length=50, blank=True, null=True)
    locations = models.ForeignKey(Locations, null=True, on_delete=models.CASCADE)
    
    # Stringfy report
    def __str__(self):
        return {
            'diseases': self.diseases,
            'syndromes': self.syndromes,
            'event_date': self.event_date,
            'locations': self.locations,
            'report_id': self.id,
            'parent_id': self.parent_id
        }

class WhatToExpect(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    travel_id = models.ForeignKey('TravelInfo', related_name="+", on_delete=models.CASCADE, null=True)
    before_your_trip = models.TextField(db_column='before_your_trip',null=True)
    on_arrival = models.TextField(db_column='on_arrival',null=True)
    quarantine_details = models.TextField(db_column='quarantine_details',null=True)
    travel_restrictions = models.TextField(db_column='travel_restrictions',null=True)

    # Stringfy report
    def __str__(self):
        return {
            'before_your_trip': self.before_your_trip,
            'on_arrival': self.on_arrival,
            'quarantine_details': self.quarantine_details,
            'travel_restrictions': self.travel_restrictions
        }

class Lanes(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    travel_id = models.ForeignKey('TravelInfo', related_name="+", on_delete=models.CASCADE, null=True)
    green = models.TextField(db_column='green',null=True)
    yellow = models.TextField(db_column='yellow',null=True)
    red = models.TextField(db_column='red',null=True)

    # Stringfy report
    def __str__(self):
        return {
            'green': self.green,
            'yellow': self.yellow,
            'red': self.red
        }
        
class Overview(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    travel_id = models.ForeignKey('TravelInfo', related_name="+", on_delete=models.CASCADE, null=True)
    open_status = models.TextField(db_column='open_status', null=True)
    quarantine_days = models.TextField(db_column='quarantine_days', null=True)

class TravelInfo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    country = models.CharField(db_column='country',max_length=50, blank=True)
    new_cases = models.CharField(db_column='new_cases', max_length=50, null=True)
    active_cases = models.CharField(db_column='active_cases', max_length=50, null=True)
    new_percentage = models.CharField(db_column='new_percentage', max_length=50, null=True)
    active_percentage = models.CharField(db_column='active_percentage', max_length=50, null=True)
    can_you_enter = models.TextField(db_column='can_you_enter',null=True)
    what_to_expect = models.ForeignKey(WhatToExpect, on_delete=models.CASCADE, null=True)
    lanes = models.ForeignKey(Lanes, on_delete=models.CASCADE, null=True)
    overview = models.ForeignKey(Overview, on_delete=models.CASCADE, null=True)

    # Stringfy report
    def __str__(self):
        return {
            'country': self.country,
            'new_cases': self.new_cases,
            'active_cases': self.active_cases,
            'new_percentage': self.new_percentage,
            'active_percentage': self.active_percentage,
            'can_you_enter': self.can_you_enter,
            'what_to_expect': self.what_to_expect
        }
