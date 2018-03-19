from availability_filter import AvailabilityFilter
from beer import Beer
from yes_filter import YesFilter


def test_name_filter_match():
    test_beer = Beer("Guinness", "pint", "stout", "5")
    fltr = AvailabilityFilter(YesFilter(), "pint")
    assert fltr.is_match(test_beer) is True
