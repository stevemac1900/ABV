#pylint: disable=too-few-public-methods
#pylint: disable=missing-docstring

class FileLocation:
    #This class allows us to abstract the location for our fetched files

    def __init__(self):
        self.current_location = "/beer_data"

    def get_file_location(self):
        "Returns the current location where we want files to be stored"
        return self.current_location
