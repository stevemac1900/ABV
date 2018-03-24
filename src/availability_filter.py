class AvailabilityFilter:
    def __init__(self, subfilter, quantity_available):
        self.subfilter = subfilter
        self.quantity_available = quantity_available

    def is_match(self, beer):
        if self.quantity_available < 1:
            return False
        return self.subfilter.is_match(beer)
