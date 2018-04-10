import requests
import logging
import os


class BreweryDBQueries:
    def __init__(self):
        pass
        # self.num_queries_today
        # self.last_query_timestamp

    def get_beer_style(self, beer_name):
        try:
            key = os.environ['BREWERYDB_API_KEY']
            request = requests.get("http://api.brewerydb.com/v2/search?key=" + key + "&q=" + beer_name + "&type=beer")
            logging.info('The request was fetched successfully!')
            if self.is_unknown(request.json()):
                return 'Unknown'
            return request.json()['data'][0]['style']['name']

        except requests.exceptions.RequestException as e:
            error_subclass = type(e).__name__
            logging.exception('The request could not be found: {}'.format(error_subclass))
            return ""

    def is_unknown(self, beer_json):
        if 'data' not in beer_json:
            return True
        if 'style' not in beer_json['data'][0]:
            return True
        beer_style = beer_json['data'][0]['style']['name']
        if len(beer_style) == 0:
            return True

        return False
