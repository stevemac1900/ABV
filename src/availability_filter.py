class AvailabilityFilter:
    def __init__(self, subfilter, availability):
        self.subfilter = subfilter
        self.availability = availability

    def is_match(self, beer):
        if beer.is_available != self.availability:
            return False
        return self.subfilter.is_match(beer)
