class SizeFilter:
    def __init__(self, subfilter, size):
        self.subfilter = subfilter
        self.size = size

    def is_match(self, beer):
        if beer.get_size != self.size:
            return False
        return self.subfilter.is_match(beer)
