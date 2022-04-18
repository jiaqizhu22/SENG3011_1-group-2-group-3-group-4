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

class TravelInfo(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    country = models.CharField(db_column='country',max_length=50, blank=True)
    new_cases = models.IntegerField(db_column='new_cases', null=True)
    active_cases = models.IntegerField(db_column='active_cases', null=True)
    new_percentage = models.DecimalField(db_column='new_percentage', max_digits=2, decimal_places=2)
    active_percentage = models.DecimalField(db_column='active_percentage', max_digits=2, decimal_places=2)
    can_you_enter = models.TextField(db_column='can_you_enter',null=True)
    what_to_expect = models.TextField(db_column='what_to_expect',null=True)

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
