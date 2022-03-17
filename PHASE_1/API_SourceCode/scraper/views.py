from django.http import HttpRequest, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.dateparse import parse_datetime

from .scraper import web_scraper
from .models import Articles, Reports, Locations
from django.utils.timezone import make_aware
from datetime import datetime

# Create your views here.

#from .models import Book, Author, BookInstance, Genre

def index(request: HttpRequest):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    #num_books = Book.objects.all().count()
    #num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    #num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    #num_authors = Author.objects.count()

    #context = {
        # 'num_books': num_books,
        # 'num_instances': num_instances,
        # 'num_instances_available': num_instances_available,
        # 'num_authors': num_authors,
    #}

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html')

def search(request: HttpRequest):
    """Search function for article database"""
    
    if request.method != "GET":
        return HttpResponseNotAllowed(request.method + " requests not allowed")
    
    start_date = make_aware(parse_datetime(request.GET.get("start_date")))
    end_date = make_aware(parse_datetime(request.GET.get("end_date")))
    
    #mid_date = start_date + (end_date - start_date) / 2
    #date_str = mid_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    location = request.GET.get("location")
    key_terms = request.GET.get("key_terms")
    if key_terms != None:
        key_terms = key_terms.split(',')
        key_terms = map(lambda x : x.lower(), key_terms)
    else:
        key_terms = []
    
    # Load scraper to get data - list of dicts
    # data = web_scraper()
    
    # Search results - articles matching parameters
    results = []

    articles = Articles.objects.filter(date_of_publication__range=(start_date, end_date))
    for article in articles:
        article_string = article.__str__()
        '''
        {
            'url': self.url,
            'date_of_publication': self.date_of_publication,
            'headline': self.headline,
            'main_text': self.main_text,
        }
        '''
        report_list = []
        reports = Reports.objects.filter(parent_id=article)
        for report in reports:
            report_string = report.__str__()
            '''
            {
                'diseases': self.diseases,
                'syndromes': self.syndromes,
                'event_date': self.event_date,
                'locations': self.locations,
                'report_id': self.id,
                'parent_id': self.parent_id
            }
            '''
            
            match_location = False
            # Find location
            location_id = report_string['locations']
            # Error: location shouldn't all be None
            print(location_id)
            location_string = {
                'country': '',
                'location': ''
            }
            if location_id != None:
                stored_location = Locations.objects.get(id=location_id)
                location_string = stored_location.__str__()
                print(location_string)
            # Check if location matches 
            if location == None or location.lower() == location_string['country'].lower() or location.lower() == location_string['location'].lower():
                match_location = True
                
            match_key_terms = False       
            if key_terms == [] or report_string['diseases'].lower() in key_terms or report_string['syndromes'].lower() in key_terms:
                match_key_terms = True

            if match_location is True or match_key_terms is True:
                report_info = {
                    'diseases': [],
                    'syndromes': [],
                    'event_date': '',
                    'locations': []
                }
                if report_string['diseases'] != None:
                    report_info['diseases'].append(report_string['diseases'])
                if report_string['syndromes'] != None:
                    report_info['syndromes'].append(report_string['syndromes'])
                # Format event_date
                if report_string['event_date'] != None:
                    report_info['event_date'] = report_string['event_date'].strftime("%Y-%m-%dT%H-%M-%S")
                if location_string != {'country': '','location': ''}:
                    report_info['locations'].append(location_string)
                    
                report_list.append(report_info)
            else:
                continue

        article_string['reports'] = report_list
        results.append(article_string)
        
    
    return JsonResponse({
        "articles": results
    })

