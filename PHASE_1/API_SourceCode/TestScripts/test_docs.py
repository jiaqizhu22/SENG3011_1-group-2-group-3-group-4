import pytest
from django.test import Client

@pytest.mark.urls('project.urls')
def test_docs_exists(client: Client):
    assert client.get('/docs/').status_code == 200