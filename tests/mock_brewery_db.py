class MockBreweryDB:
    def get_beer_style(self, beer_name):
        if beer_name == "Guiness":
            return "stout"
        assert False

class MockBreweryDBAlwaysStout:
    def get_beer_style(beer_name):
        return "stout"

class MockBreweryDBAlwaysError:
    count = 0
    def get_beer_style(cls, beer_name):
        cls.count += 1
        raise Exception('Error')
