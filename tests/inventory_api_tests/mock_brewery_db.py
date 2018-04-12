# pylint: disable=unused-argument

class MockBreweryDBUnknownTracked:
    count = 0
    def get_beer_style(self, beer_name):
        self.count += 1
        return "Unknown"

class MockBreweryDBStoutTracked:
    count = 0
    def get_beer_style(self, beer_name):
        self.count += 1
        return "stout"

class MockBreweryDBAlwaysError:
    count = 0
    def get_beer_style(self, beer_name):
        self.count += 1
        raise Exception('Error')
