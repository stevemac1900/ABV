'File which contains NameFilter class'
class NameFilter:

    def __init__(self, subfilter, name):
        'Intializes name filter'
        self.subfilter = subfilter
        self.name = name


    def is_match(self, beer):
        'Checks to see if the beer object name matches the name which is passed through name filter'
        if beer.name != self.name:
            return False
        return self.subfilter.is_match(beer)
