"StyleFilter will create a filter to see if the beer in question has the style of the query"

#pylint: disable=missing-docstring
class StyleFilter:

    # pylint: disable=too-few-public-methods

    def __init__(self, subfilter, style):
        "Constructor for the style filter"
        self.subfilter = subfilter
        self.style = style

    def is_match(self, beer):
        "Tests if the beer has the same style as the filter."
        if beer.style != self.style:
            return False
        return self.subfilter.is_match(beer)
