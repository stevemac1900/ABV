from abv.inventory_api.style_db import StyleDB
from abv.inventory_api.style_cache import StyleCache
from tests.inventory_api_tests import mock_brewery_db


def test_cache_has_beer():
    styles = StyleDB()
    styles.cache = StyleCache('tests/sample_csv_files/beer_and_style.csv')
    styles.brew_db = mock_brewery_db.MockDB()
    assert styles.get_style('Nitro') == 'Stout'
    assert styles.brew_db.count == 0


def test_db_has_style_and_then_cache():
    styles = StyleDB()
    styles.cache = StyleCache('tests/sample_csv_files/beer_and_style.csv')
    styles.brew_db = mock_brewery_db.MockDB()
    assert styles.get_style('Guinness') == 'Stout'
    assert styles.get_style('Guinness') == 'Stout'
    assert styles.brew_db.count == 0


def test_unknown_from_db_then_cache():
    styles = StyleDB()
    styles.cache = StyleCache('tests/sample_csv_files/beer_and_style.csv')
    styles.brew_db = mock_brewery_db.MockDB()
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.get_style('Duck Tails') == 'Unknown'
    assert styles.brew_db.count == 0


def test_two_against_db():
    styles = StyleDB()
    styles.cache = StyleCache('tests/sample_csv_files/beer_and_style.csv')
    styles.brew_db = mock_brewery_db.MockDB()
    assert styles.get_style('xyz') == "Unknown"
    assert styles.get_style('xyz') == "Unknown"
    assert styles.brew_db.count == 2
