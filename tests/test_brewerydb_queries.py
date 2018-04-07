import pytest
import requests
import requests_mock
from abv.brewerydb_queries import BreweryDBQueries

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


url = 'http://api/search?key=1&q=Guinness'


@pytest.fixture()
def no_name():
    with requests_mock.Mocker() as session:
        session.get(url, json={'status': 'success'})
        yield


@pytest.fixture()
def no_style():
    with requests_mock.Mocker() as session:
        session.get(url, json={'status': 'success', 'data': [{}]})
        yield


@pytest.fixture()
def no_style_result():
    with requests_mock.Mocker() as session:
        session.get(url, json={'status': 'success', 'data': [{'style': {'name': ''}}]})
        yield


@pytest.fixture()
def single_result():
    with requests_mock.Mocker() as session:
        session.get(url, json={'status': 'success', 'data': [{'style': {'name': 'Stout'}}]})
        yield


# Exception would be thrown when the "status" key has "failure" value
@pytest.fixture(params=[requests.exceptions.RequestException])
def failed_request(request):
    with requests_mock.Mocker() as session:
        session.get('http://api/search?key=1&q=Guinness', exc=request.param)

        yield request.param


def test_no_name(no_name):
    queries = BreweryDBQueries(API_KEY='1')
    style = queries.get_beer_style('Guinness')
    assert style == 'Unknown'


def test_no_style(no_style):
    queries = BreweryDBQueries(API_KEY='1')
    style = queries.get_beer_style('Guinness')
    assert style == 'Unknown'


def test_no_style_result(no_style_result):
    queries = BreweryDBQueries(API_KEY='1')
    style = queries.get_beer_style('Guinness')
    assert style == 'Unknown'


def test_single_result(single_result):
    queries = BreweryDBQueries(API_KEY='1')
    style = queries.get_beer_style('Guinness')
    assert style == 'Stout'


def test_failed_request(failed_request):
    queries = BreweryDBQueries(API_KEY='1')
    style = queries.get_beer_style('Guinness')
    assert style == ''
