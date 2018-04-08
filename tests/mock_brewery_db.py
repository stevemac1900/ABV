

class MockBreweryDBAlwaysUnknown:
    def get_beer_style(self, beer_name):
        return "Unknown"


class MockBreweryDBAlwaysStout:
    def get_beer_style(beer_name):
        return "stout"

class MockBreweryDBAlwaysError:
    count = 0
    def get_beer_style(cls, beer_name):
        print("count1:" + str(cls.count))
        cls.count += 1
        print("count2:" + str(cls.count))
        raise Exception('Error')
