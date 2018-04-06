from tests import mock_brewery_db

class StyleDB():
    def __init__(self, beer_dict, brew_db):
        self.beer_dict = beer_dict
        self.brew_db = brew_db

    def getStyle(self, name):
        if name in self.beer_dict:
            return self.beer_dict[name]
        self.beer_dict[name] = self.brew_db.get_beer_style(name)
        return self.brew_db.get_beer_style(name)