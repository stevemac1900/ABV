import pytest
import requests
import requests_mock
from abv.inventory_api.brewerydb_queries import BreweryDBQueries
import os
# happy path
# 0 results: don't try again
# no name/style: return unknown
# server is down: throw exception
# should we distinguish between try again b/c rate limit or b/c server is down?
# implement a counter that handles up to 400 requests in a day EST
# # hit the 400 requests per day if clocks are on different times: throw exception
# return error code statement for anything that's not 200
    # 400
    # 401 -- bad key input
    # 404 -- bad endpoint


BREWERY_DB_URL = "http://api.brewerydb.com/v2/search?key="+ os.environ['BREWERYDB_API_KEY'] + "&q=Guinness&type=beer"
QUERIES = BreweryDBQueries()

@pytest.fixture()
def no_name():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success'})
        yield


@pytest.fixture()
def no_style():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data': [{}]})
        yield


@pytest.fixture()
def no_style_result():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data': [{'style': {'shortName': ''}}]})
        yield


@pytest.fixture()
def single_result():
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, json={'status': 'success', 'data': [{'style': {'shortName': 'Stout'}}]})
        yield


# Exception would be thrown when the "status" key has "failure" value
@pytest.fixture(params=[requests.exceptions.RequestException])
def failed_request(request):
    with requests_mock.Mocker() as session:
        session.get(BREWERY_DB_URL, exc=request.param)

        yield request.param


def test_no_name(no_name):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Unknown'


def test_no_style(no_style):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Unknown'


def test_no_style_result(no_style_result):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Unknown'


def test_single_result(single_result):
    style = QUERIES.get_beer_style('Guinness')
    assert style == 'Stout'


def test_failed_request(failed_request):
    style = QUERIES.get_beer_style('Guinness')
    assert style == ''