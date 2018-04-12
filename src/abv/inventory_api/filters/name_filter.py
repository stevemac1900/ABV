class NameFilter:

    def __init__(self, subfilter, name):
        self.subfilter = subfilter
        self.name = name

    def is_match(self, beer):
        if beer.name != self.name:
            return False
        return self.subfilter.is_match(beer)
