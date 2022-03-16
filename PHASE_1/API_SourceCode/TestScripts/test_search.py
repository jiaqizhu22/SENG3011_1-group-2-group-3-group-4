from random import sample
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
def test_search_get_empty(client: Client):
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
    assert len(parsedData["results"]) == 0
    