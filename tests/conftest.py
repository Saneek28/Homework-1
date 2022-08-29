import pytest

from src.dog_api_client import DogApiClient
from src.jsonplaceholder_client import JsonPlaceholderClient
from src.openbrewerydb_api_client import OpenBreweryDBClient


def pytest_addoption(parser):
    parser.addoption(
        "--url", action="store", default="https://ya.ru", type=str, help="url to make a request"
    )
    parser.addoption(
        "--status_code", action="store", default=200, type=int, help="expected status code"
    )


@pytest.fixture(scope='class')
def dog_client():
    return DogApiClient()


@pytest.fixture(scope='class')
def openbrewerydb_client():
    return OpenBreweryDBClient()


@pytest.fixture(scope='class')
def jsonplaceholder_client():
    return JsonPlaceholderClient()


@pytest.fixture(scope='function')
def created_resource(jsonplaceholder_client):
    resource = {'way': 'the is no way'}
    return jsonplaceholder_client.create_resource(data=resource)
