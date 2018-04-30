# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from abv.inventory_api.brewerydb_queries import BreweryDBQueries
from abv.inventory_api.style_cache import StyleCache


class StyleDB:

    def __init__(self):
        self.cache = StyleCache('src/abv/inventory_api/beer_styles.csv')
        self.brew_db = BreweryDBQueries()

    def get_style(self, beer_name):
        beer_name = beer_name.title()
        if self.cache.look_up(beer_name) is not None:
            return self.cache.cache_dict[beer_name]
        try:
            style = self.brew_db.get_beer_style(beer_name)
            self.cache.add(beer_name, style)
            return style
        # pylint: disable=broad-except
        except Exception:
            return 'Unknown'
