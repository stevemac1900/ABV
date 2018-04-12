# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from tests import mock_brewery_db

class StyleDB:
    #This class creates a database that stores beer styles
    def __init__(self):
        self.style_dict = {}
        self.brew_db = mock_brewery_db.MockBreweryDBStoutTracked #Need to make a stub for a fake Brewery DB

    def get_style(self, name):
        #Returns the style of a beer
        if name in self.style_dict:
            return self.style_dict[name]
        try:
            style = self.brew_db.get_beer_style(name)
            self.style_dict[name] = style
            return style
        # pylint: disable=broad-except
        except Exception:
            return 'Unknown'
