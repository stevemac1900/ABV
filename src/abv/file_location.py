class FileLocation:

    def __init__(self):
        self.current_location = "../../beer_data/"

    def get_file_location(self):
        "Returns the current location where we want files to be stored"
        return self.current_location
