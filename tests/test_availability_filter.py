from availability_filter import AvailabilityFilter
from beer import Beer
from yes_filter import YesFilter


def get_test_beer(quantity):
    return Beer("Guinness", "pint", "stout", quantity)


def test_quantity_filter_positive_value():
    get_test_beer(5)
    fltr = AvailabilityFilter(YesFilter(), "pint")
    assert fltr.is_match(test_beer) is True


def test_quantity_filter_zero_value():
    get_test_beer(0)
    fltr = AvailabilityFilter(YesFilter(), "pint")
    assert fltr.is_match(test_beer) is True


def test_quantity_filter_negative_value():
    get_test_beer(-5)
    fltr = AvailabilityFilter(YesFilter(), "pint")
    assert fltr.is_match(test_beer) is True
