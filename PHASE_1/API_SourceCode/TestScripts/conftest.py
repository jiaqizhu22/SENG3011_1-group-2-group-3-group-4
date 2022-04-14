import pytest

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

@pytest.fixture(scope='session')
def django_db_setup():
    pass

@pytest.fixture
def db_access_without_rollback_and_truncate(request, django_db_setup, django_db_blocker):
    django_db_blocker.unblock()
    request.addfinalizer(django_db_blocker.restore)
