from availability_filter import AvailabilityFilter
from beer import Beer
from yes_filter import YesFilter


def get_test_beer(quantity):
    return Beer("Guinness", "pint", "stout", quantity)


def test_quantity_filter_positive_value():
    fltr = AvailabilityFilter(YesFilter(), 5)
    assert fltr.is_match(get_test_beer(5)) is True


def test_quantity_filter_zero_value():
    fltr = AvailabilityFilter(YesFilter(), 0)
    assert fltr.is_match(get_test_beer(0)) is True


def test_quantity_filter_negative_value():
    fltr = AvailabilityFilter(YesFilter(), -5)
    assert fltr.is_match(get_test_beer(-5)) is True
