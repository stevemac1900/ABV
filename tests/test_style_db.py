from tests.mock_brewery_db import MockBreweryDBAlwaysStout
from tests.mock_brewery_db import MockBreweryDBAlwaysError
from tests.mock_styledb import StyleDB
from tests.mock_brewery_db import MockBreweryDBAlwaysUnknown
import pytest


#Tests that stout is correctly returned when cache has it
def test_cache_has_beer():
    styles_dict = {'Nitro': 'stout'}
    styles_brewery_db = MockBreweryDBAlwaysStout()
    styles = StyleDB(styles_dict,styles_brewery_db)
    assert styles.getStyle('Nitro') == 'stout'

#Tests if the database has the style and not the cache
def test_db_has_style():
    styles_dict = {}
    styles_brewery_db = MockBreweryDBAlwaysStout()
    styles = StyleDB(styles_dict, styles_brewery_db)
    assert styles.getStyle('Guiness') == 'stout'

#Tests that looks up once in database if cache doesnt have and then not again (now in cache)
def test_searches_database_only_once():
    styles_dict = {}
    styles_brewery_db = MockBreweryDBAlwaysUnknown()
    styles = StyleDB(styles_dict, styles_brewery_db)
    assert styles.getStyle("Duck Tails") == "Unknown"
    assert styles.beer_dict["Duck Tails"] == "Unknown"

#Tests that if query throws error once, that it throws it again by same input
def test_two_against_db():
    style_dict = {}
    mocked_db = MockBreweryDBAlwaysError()
    styles = StyleDB(style_dict, mocked_db)
    with pytest.raises(Exception):
        assert styles.getStyle('Guiness') == "Unknown"
        assert styles.getStyle('Guiness') == "Unknown"
    assert mocked_db.count == 2
