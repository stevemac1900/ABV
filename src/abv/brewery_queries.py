import requests
import os

class BreweryQueries:

    def get_beer_style(self, beer_name):
        key = os.environ['BREWERYDB_API_KEY']
        url = "http://api.brewerydb.com/v2/search?key=" + key + "&q=" + beer_name + "&type=beer"
        r = requests.get(url)
        return r.json()["data"][0]["style"]["name"]
