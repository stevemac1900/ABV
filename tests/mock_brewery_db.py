class MockBreweryDB:
    def get_beer_style(beer_name):
        if beer_name is None:
         assert False
        return "Stout"