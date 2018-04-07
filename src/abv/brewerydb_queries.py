import requests
import logging


class BreweryDBQueries:
    def __init__(self, API_KEY):
        self.API_KEY = API_KEY
        # self.num_queries_today
        # self.last_query_timestamp

    def get_beer_style(self, beer_name):
        try:
            request = requests.get('http://api/search?key=' + self.API_KEY + '&q=' + beer_name)
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
