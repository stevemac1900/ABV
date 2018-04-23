from tests.inventory_api_tests.mock_inventory_queries import MockInventoryQueries
from abv.inventory_api.beer import Beer
import abv.inventory_api.beerapi as beerapi
from tests.inventory_api_tests.mock_inventory_queries_saving import MockInventoryQueriesSaving
from abv.file_location import FileLocation

beerapi.app.testing = True
app = beerapi.app.test_client()

pabst = Beer(name='Pabst', size='12/12oz', style='lager', quantity='1', price='20')
guinness = Beer(name='Guinness', size='12/12oz', style='stout', quantity='1', price='30')


def test_empty_results():
    beerapi.queries = MockInventoryQueries([])
    result = app.get('/current')
    assert result.data == b'[]'


def test_single_result():
    beerapi.queries = MockInventoryQueries([pabst])
    result = app.get('/current')
    assert eval(result.data)[0]['name'] == 'Pabst'


def test_two_results():
    beerapi.queries = MockInventoryQueries([pabst, guinness])
    result = app.get('/current')
    assert eval(result.data)[0]['name'] == 'Pabst'
    assert eval(result.data)[1]['name'] == 'Guinness'

def test_no_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    app.get('/current')
    assert saver.filter.name is None
    assert saver.filter.style is None


def test_name_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    app.get('/current?name=Guinness')
    assert beerapi.queries.filter.name == 'Guinness'
    assert saver.filter.style is None


def test_availability_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    app.get('/current?name=Guinness&availability=2')
    assert saver.filter.name == 'Guinness'
    assert saver.filter.availability == '2'
    assert saver.filter.style == None


def test_style_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    app.get('/current?name=Guinness&availability=2&style=stout')
    assert saver.filter.name == 'Guinness'
    assert saver.filter.availability == '2'
    assert saver.filter.style == 'stout'
    assert saver.filter.size is None


def test_size_filter():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    app.get('/current?name=Guinness&availability=2&style=stout&size=12/12OZ')
    assert saver.filter.name == 'Guinness'
    assert saver.filter.availability == '2'
    assert saver.filter.style == 'stout'
    assert saver.filter.size == '12/12OZ'


def test_repeat_params():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    app.get('/current?name=Guinness&name=Pabst')
    assert saver.filter.name == 'Guinness'


def test_bad_params():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    result = app.get('/current?foo=bar')
    assert result.status_code == 400


def test_bad_and_good_params():
    saver = MockInventoryQueriesSaving()
    beerapi.queries = saver
    result = app.get('/current?name=Guinness&foo=bar')
    assert result.status_code == 400


def test_api_initialization():
    FileLocation.save_location = 'tests/sample_csv_files'
    beerapi.initialize_inventory()
    assert beerapi.queries.inventory.get_historic_inventory()[0].name == 'BREW WORKS HOP EXPLOSION'
