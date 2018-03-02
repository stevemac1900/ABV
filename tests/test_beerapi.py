import pytest
import requests
import requests_mock
import src.beerapi as beerapi



#TODO: Make this test of success work with the current code of beerapi somehow
@pytest.fixture()
def expected_success():
    with requests_mock.Mocker() as session:
        session.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv', text = 'success')
        yield


@pytest.fixture(params= [requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError])
def expected_exception(request):
    with requests_mock.Mocker() as session:
        session.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv', exc = request.param)
        yield request.param

def test_connection_exceptions(expected_exception):
    with pytest.raises(expected_exception):
        beerapi.write_beer_inventory();
