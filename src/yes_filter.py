"""This module contains the base class for the database filters"""
#pylint: disable=unused-argument

class YesFilter:
    "This is the base class of our filter"
    @classmethod
    def is_match(self, beer):
        "This method returns true for any beer"
        return True
