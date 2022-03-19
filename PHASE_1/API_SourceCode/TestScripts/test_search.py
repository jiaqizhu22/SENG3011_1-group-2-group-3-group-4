import pytest
from django.test import Client
import json

@pytest.mark.urls('project.urls')
def test_search_invalidmethods(client: Client):
    assert client.post('/search/').status_code == 405
    assert client.put('/search/').status_code == 405
    assert client.delete('/search/').status_code == 405
    assert client.options('/search/').status_code == 405
    assert client.trace('/search/').status_code == 405
    assert client.patch('/search/').status_code == 405
    
@pytest.mark.urls('project.urls')
def test_search_invalidinput_date(client: Client):
    # Test end and start dates separately
    sampleSearch = {
        "start_date": "not-a-real-date",
        "end_date": "2015-10-01T09:45:10",
        "location": "Morocco",
        "key_terms": [
            "Spanish Flu",
            "Outbreak"
        ],
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 400
    
    sampleSearch = {
        "start_date": "2015-10-01T09:45:10",
        "end_date": "not-a-real-date",
        "location": "Morocco",
        "key_terms": [
            "Spanish Flu",
            "Outbreak"
        ],
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 400
    
    

@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_empty_valid(client: Client):
    sampleSearch = {
        "start_date": "2015-10-01T08:45:10",
        "end_date": "2015-10-01T09:45:10",
        "location": "Morocco",
        "key_terms": [
            "Spanish Flu",
            "Outbreak"
        ],
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be no results for this query
    assert len(parsedData["articles"]) == 0
    
@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_empty_wrongorder(client: Client):
    # Start date is after end date
    sampleSearch = {
        "start_date": "2016-10-01T09:45:10",
        "end_date": "2015-10-01T08:45:10",
        "location": "Morocco",
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be no results for this query
    assert len(parsedData["articles"]) == 0
    
@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_empty_equaltime(client: Client):
    # Start date is equal to end date
    sampleSearch = {
        "start_date": "2015-10-01T08:45:10",
        "end_date": "2015-10-01T08:45:10",
        "location": "Morocco",
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be no results for this query
    assert len(parsedData["articles"]) == 0
    
@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_empty_nolocation(client: Client):
    # Not a real location
    sampleSearch = {
        "start_date": "2015-10-01T08:45:10",
        "end_date": "2020-10-01T08:45:10",
        "location": "NotARealLocationia",
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be no results for this query
    assert len(parsedData["articles"]) == 0

@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_empty_nokeyterms(client: Client):
    # Not real key terms
    sampleSearch = {
        "start_date": "2015-10-01T08:45:10",
        "end_date": "2020-10-01T08:45:10",
        "location": "Australia",
        "key_terms": [
            "jasdmajdjasdmjkasdmajdkmasjd"
        ],
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be no results for this query
    assert len(parsedData["articles"]) == 0

@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_one_valid_oldformat(client: Client):
    # Valid input for an outbreak in the old format
    sampleSearch = {
        "start_date": "2003-3-6T01:00:00",
        "end_date": "2003-3-8T01:00:00",
        "location": "Burkina Faso",
        "key_terms": [
            "Meningococcal"
        ],
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be one result for this query
    assert len(parsedData["articles"]) == 1
    
    article = parsedData["articles"][0]
    assert article["url"] == "https://www.who.int/emergencies/disease-outbreak-news/item/2003_03_7a-en"
    assert article["date_of_publication"] == "2003-3-7"
    assert article["headline"] == "Meningococcal disease in Burkina Faso - Update 3"
    assert article["main_text"][0:25] == "As of 6 March, the Ministry of Health of Burkina Faso has reported a total"[0:25]
    
@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_one_valid_newformat(client: Client):
    # Valid input for an outbreak in the new format
    sampleSearch = {
        "start_date": "2022-1-24T01:00:00",
        "end_date": "2022-1-26T01:00:00",
        "location": "Benin",
        "key_terms": [
            "Cholera"
        ],
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be one result for this query
    assert len(parsedData["articles"]) == 1
    
    article = parsedData["articles"][0]
    assert article["url"] == "https://www.who.int/emergencies/disease-outbreak-news/item/cholera-benin"
    assert article["date_of_publication"] == "2022-1-25"
    assert article["headline"] == "Cholera – Benin"
    assert article["main_text"][0:25] == "Cholera is endemic in Benin with cases reported annually since 2016. In 2021, Benin"[0:25]
    
@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_one_difflocations(client: Client):
    # There are 2 in this date range, only one in this location
    sampleSearch = {
        "start_date": "2022-1-24T01:00:00",
        "end_date": "2022-2-5T01:00:00",
        "location": "Benin",
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be one result for this query
    assert len(parsedData["articles"]) == 1
    
    # Test the other location
    sampleSearch["location"] = "Timor-Leste"
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be one result for this query
    assert len(parsedData["articles"]) == 1
    
@pytest.mark.urls('project.urls')
@pytest.mark.django_db
def test_search_get_multiple(client: Client):
    # There are many in this date range
    sampleSearch = {
        "start_date": "2022-6-18T01:00:00",
        "end_date": "2022-9-18T01:00:00",
        "location": "Guinea",
    }
    
    result = client.get('/search/', data=sampleSearch)
    
    assert result.status_code == 200
    
    parsedData = json.loads(result.content)
    
    # There should be one result for this query
    assert len(parsedData["articles"]) == 3
    
