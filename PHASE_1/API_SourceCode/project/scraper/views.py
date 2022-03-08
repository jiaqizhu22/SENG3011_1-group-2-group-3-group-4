from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the index page for the scraper API.")