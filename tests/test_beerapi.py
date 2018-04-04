import pytest
import requests
import requests_mock
import abv.beerapi as beerapi

TANCZOS_INVENTORY = 'http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv'


@pytest.fixture(params=[requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError])
def expected_exception_on_read(request):
    with requests_mock.Mocker() as session:
        session.get(TANCZOS_INVENTORY, exc=request.param)
        yield request.param


# pylint: disable=redefined-outer-name, unused-argument
def test_connection_exceptions_on_read(expected_exception_on_read):
    assert beerapi.get_inventory() == ""


@pytest.fixture(params=[OSError])
def expected_exception_on_write(request):
    with requests_mock.Mocker() as session:
        session.get(TANCZOS_INVENTORY, exc=request.param)
        yield request.param


# pylint: disable=redefined-outer-name
def test_exception_on_write(expected_exception_on_write):
    with pytest.raises(expected_exception_on_write):
        beerapi.write_beer_inventory()
