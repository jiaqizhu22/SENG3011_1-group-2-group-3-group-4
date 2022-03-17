from django.http import HttpRequest, JsonResponse, HttpResponseNotAllowed
from django.shortcuts import render
from django.utils.dateparse import parse_datetime

from .scraper import web_scraper
from .models import Articles, Reports, Locations

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
    
    start_date = parse_datetime(request.GET.get("start_date"))
    end_date = parse_datetime(request.GET.get("end_date"))
    
    #mid_date = start_date + (end_date - start_date) / 2
    #date_str = mid_date.strftime("%Y-%m-%dT%H:%M:%S")
    
    location = request.GET.get("location")
    key_terms = request.GET.get("key_terms").split(',')
    
    # Load scraper to get data - list of dicts
    # data = web_scraper()
    
    # Search results - articles matching parameters
    results = []

    #title_str = "Outbreak in " + str(location)
    #link = "fake-article.com/" + title_str.lower().replace(' ', '-') + '-' + '-'.join(key_terms).replace(' ', '-')

    articles = Articles.objects.filter(data_of_publication__range=(start_date, end_date))
    for article in articles:
        reports = Reports.objects.filter(parent_id=article)
        for report in reports:
            if report.diseases in key_terms:
                results.append(article)
            elif report.syndromes in key_terms:
                results.append(article)
            else:
                results.append(article)
    
    
    
    
    return JsonResponse({
        "articles": [results]
    })

