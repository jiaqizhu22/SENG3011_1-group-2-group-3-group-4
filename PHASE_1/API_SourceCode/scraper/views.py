from django.http import HttpRequest, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.dateparse import parse_datetime

from .scraper import web_scraper
from .models import Articles, Reports, Locations
from django.utils.timezone import make_aware

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
    
    # Load scraper to get data - list of dicts
    # data = web_scraper()
    
    # Search results - articles matching parameters
    results = []

    #title_str = "Outbreak in " + str(location)
    #link = "fake-article.com/" + title_str.lower().replace(' ', '-') + '-' + '-'.join(key_terms).replace(' ', '-')

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
        '''
        for report in reports:
            if report.diseases in key_terms:
                results.append(article)
            elif report.syndromes in key_terms:
                results.append(article)
            else:
                results.append(article)
        '''
        for report in reports:
            report_string = report.__str__()
            # Find location
            location_id = int(report_string['locations'])
            location = Locations.objects.get(id=location_id)
            print(location_id)
            print(location)
            location_string = location.__str__()
            report_info = {
                'diseases': [report_string['diseases']],
                'syndromes': [report_string['syndromes']],
                'event_date': report_string['event_date'],
                'locations': [location_string]
            }
            report_list.append(report_info)
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
        article_string['reports'] = report_list
        results.append(article_string)
        
    
    return JsonResponse({
        "articles": [results]
    })

