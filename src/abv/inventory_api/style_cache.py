
"""This class creates a style cache that holds recently searched for beers."""
class StyleCache:

    """Cache constructor."""
    def __init__(self, filename):
        self.filename = filename
        self.cache_dict = {}

        with open(self.filename, 'r') as infile:
            i = 0
            for line in infile:
                if i == 0:
                    i += 1
                    continue
                line = line.strip()
                beer_data = line.split(',')
                self.cache_dict[beer_data[0]] = beer_data[1]

    def look_up(self, beer_name):
        """Beer look up method """
        if beer_name in self.cache_dict:
            return str(self.cache_dict[beer_name])
        return None

    def add(self, beer, style):
        """Adds the searched beer to the file"""
        self.cache_dict[beer] = style
        with open(self.filename, "a") as myfile:
            myfile.write(beer + ',' + style + '\n')
