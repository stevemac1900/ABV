# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods


class StyleDB():
    #This class creates a database that stores beer styles
    def __init__(self, beer_dict, brew_db):
        self.beer_dict = beer_dict
        self.brew_db = brew_db

    def get_style(self, name):
        #Returns the style of a beer
        if name in self.beer_dict:
            return self.beer_dict[name]
        try:
            style = self.brew_db.get_beer_style(name)
            self.beer_dict[name] = style
            return style
        # pylint: disable=broad-except
        except Exception:
            return 'Unknown'
