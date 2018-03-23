from availability_filter import AvailabilityFilter
from beer import Beer
from yes_filter import YesFilter


def get_test_beer(quantity):
    return Beer("Guinness", "pint", "stout", 0, quantity)


def get_test_filter(quantity):
    return AvailabilityFilter(YesFilter(), quantity)


def test_quantity_filter_positive_value():
    assert get_test_filter(5).is_match(get_test_beer(5)) is True


def test_quantity_filter_zero_value():
    assert get_test_filter(0).is_match(get_test_beer(0)) is False


def test_quantity_filter_negative_value():
    assert get_test_filter(-5).is_match(get_test_beer(-5)) is False

