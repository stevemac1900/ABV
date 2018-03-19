import pytest
import requests
import requests_mock
import src.beerapi as beerapi


@pytest.fixture(params= [requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError])
def expected_exception_on_read(request):
    with requests_mock.Mocker() as session:
        session.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv', exc=request.param)
        yield request.param


def test_connection_exceptions_on_read(expected_exception_on_read):
    assert beerapi.get_inventory() is ""


@pytest.fixture()
def expected_exception_on_write():
    with requests_mock.Mocker() as session:
        session.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv', exc=OSError)
        yield


def test_exception_on_write(expected_exception_on_write):
    with pytest.raises(OSError):
        beerapi.write_beer_inventory();

