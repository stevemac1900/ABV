"""This module contains the base class for the database filters"""

class YesFilter:
    "This is the base class of our filter"

    # pylint: disable=unused-argument
    @classmethod
    def is_match(cls, beer):
        "This method returns true for any beer"
        return True
