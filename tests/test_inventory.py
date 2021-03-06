
from inventory import Inventory
import pytest

def inventory_has_proper_size(filename, size):
    base_dir = 'sample_csv_files/'
    i = Inventory(base_dir + filename)
    assert size == len(i.get_historic_inventory())


def test_empty_inventory():
    inventory_has_proper_size('empty.csv', 0)


def test_single_item_inventory():
    inventory_has_proper_size('single.csv', 1)


def test_many_items():
    inventory_has_proper_size('three.csv', 3)


def test_load_numeric_fields():
    i = Inventory('sample_csv_files/single.csv')
    values = i.get_historic_inventory()[0]

    assert pytest.approx(0) == values['quantity']
    assert pytest.approx(182.99) == values['price']
    assert pytest.approx(182.99) == values['case_price']
    assert pytest.approx(1) == values['case_pack']

def test_load_convert_case():
    i = Inventory('sample_csv_files/single.csv')
    values = i.get_historic_inventory()[0]

    assert 'Bells Best Brown' == values['name']
    assert '1/2 Keg' == values['size']
    assert 'Craft' == values['category']