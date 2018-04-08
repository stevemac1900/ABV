import requests_mock
from abv.brewery_queries import BreweryQueries
import os
import json

def test_one_beer():
    with requests_mock.Mocker() as m:
        os.environ['BREWERYDB_API_KEY'] = 'mock_key'
        beer = json.dumps({'data': [{'style':{"name":"stout"}}]})
        m.get("http://api.brewerydb.com/v2/search?key=mock_key&q=Guinness" + "&type=beer", text=str(beer))
        query = BreweryQueries()
        assert query.get_beer_style('Guinness') == "stout"
