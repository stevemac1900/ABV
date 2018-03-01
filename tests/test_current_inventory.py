
from available_inventory import get_available_inventory


def test_no_inventory():
    assert [] == get_available_inventory()
