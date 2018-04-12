from tests.inventory_api_tests.mock_brewery_db import MockBreweryDBStoutTracked
from tests.inventory_api_tests.mock_brewery_db import MockBreweryDBAlwaysError
from tests.inventory_api_tests.mock_brewery_db import MockBreweryDBUnknownTracked
from abv.inventory_api.style_db import StyleDB


def test_cache_has_beer():
    styles_dict = {'Nitro': 'stout'}
    styles_brewery_db = MockBreweryDBStoutTracked()
    styles = StyleDB(styles_dict, styles_brewery_db)
    assert styles.get_style('Nitro') == 'stout'
    assert styles.brew_db.count == 0


def test_db_has_style_and_then_cache():
    styles_dict = {}
    styles_brewery_db = MockBreweryDBStoutTracked()
    styles = StyleDB(styles_dict, styles_brewery_db)
    tested = styles.get_style('Guinness')
    print(tested)
    assert styles.get_style('Guinness') == 'stout'
    assert styles.get_style('Guinness') == 'stout'
    assert styles.brew_db.count == 1


def test_unknown_from_db_then_cache():
    styles_dict = {}
    styles_brewery_db = MockBreweryDBUnknownTracked()
    styles = StyleDB(styles_dict, styles_brewery_db)
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.brew_db.count == 1


def test_two_against_db():
    """ Tests that if query throws error once, that it throws it again by same input """
    style_dict = {}
    mocked_db = MockBreweryDBAlwaysError()
    styles = StyleDB(style_dict, mocked_db)
    assert styles.get_style('Guinness') == "Unknown"
    assert styles.get_style('Guinness') == "Unknown"
    assert mocked_db.count == 2
