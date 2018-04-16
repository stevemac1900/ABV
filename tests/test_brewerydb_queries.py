import pytest
import requests
import requests_mock
import os
from abv.brewerydb_queries import BreweryDBQueries

key = os.environ['BREWERYDB_API_KEY']
BREWERY_DB_URL = 'http://api.brewerydb.com/v2/search?key=' + key + '&q=Guinness&type=beer'
QUERIES = BreweryDBQueries()


@pytest.fixture()
def no_name():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success'})
        yield


def test_no_name(no_name):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Unknown'


@pytest.fixture()
def no_style():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data': [{}]})
        yield


def test_no_style(no_style):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Unknown'


@pytest.fixture()
def no_style_result():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data':
            [{'style': {'name': '', 'shortName': ''}}]})
        yield


def test_no_style_result(no_style_result):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Unknown'


@pytest.fixture()
def no_short_name_for_style():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data':
            [{'style': {'name': 'Irish Imperial Stout', 'shortName': ''}}]})
        yield


def test_no_short_name_for_style(no_short_name_for_style):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Irish Imperial Stout'


@pytest.fixture()
def single_result():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data':
            [{'style': {'name': 'Irish Imperial Stout', 'shortName': 'Stout'}}]})
        yield


def test_single_result(single_result):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Stout'


@pytest.fixture(params=[requests.exceptions.RequestException])
def failed_request(request):
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, exc=request.param)
        yield request.param


def test_failed_request(failed_request):
    QUERIES.get_beer_style('Guinness')


@pytest.fixture(params=[requests.exceptions.RequestException])
def request_count_close_to_limit(request):
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, exc=request.param)
        yield request.param


def test_request_limit(request_count_close_to_limit):
    QUERIES.get_beer_style('Guinness')
    QUERIES.num_queries_today = 390
