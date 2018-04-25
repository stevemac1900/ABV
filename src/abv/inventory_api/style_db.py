# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from tests.inventory_api_tests import mock_brewery_db


class StyleDB:

    def __init__(self):
        self.style_dict = {'Nitro':'stout'}
        self.brew_db = mock_brewery_db.MockDB()

    def get_style(self, beer_name):

        if beer_name in self.style_dict:
            return self.style_dict[beer_name]
        try:
            style = self.brew_db.get_style(beer_name)
            self.style_dict[beer_name] = style
            return style
        # pylint: disable=broad-except
        except Exception:
            return 'Unknown'
