class AvailabilityFilter:
    def __init__(self, subfilter, quantity_available):
        self.sf = subfilter
        self.qa = quantity_available

    def is_match(self, beer):
        if self.qa < 1:
            return False
        return self.sf.is_match(beer)
