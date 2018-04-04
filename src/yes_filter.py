""" This module contains the base class for the database filters """


class YesFilter:
    # pylint: disable=unused-argument
    @classmethod
    def is_match(cls, beer):
        return True
