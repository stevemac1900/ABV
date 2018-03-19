from size_filter import SizeFilter
from beer import Beer
from yes_filter import YesFilter


def test_name_filter_match():
    test_beer = Beer("Guinness", "pint", "stout", "5")
    fltr = SizeFilter(YesFilter(), "pint")
    assert fltr.is_match(test_beer) is True
