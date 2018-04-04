from abv.available_inventory import InventoryQueries
from abv.inventory import Inventory
from abv.name_filter import NameFilter
from abv.yes_filter import YesFilter

BASE_DIR = "tests/sample_csv_files/"


def make_test_name_filter(beer_name):
    return NameFilter(YesFilter(), beer_name)


def make_test_inventory_query(test_file):
    test_file = test_file
    inventory = Inventory(BASE_DIR + test_file)
    return InventoryQueries(inventory)


def test_one_beer_name_filter_true():
    query = make_test_inventory_query("single_positive_quantity.csv")
    name_filter = make_test_name_filter("Bells Best Brown")
    assert query.get_filtered_inventory(name_filter)[0].get_name() == "Bells Best Brown"


def test_one_beer_name_filter_false():
    query = make_test_inventory_query("single_positive_quantity.csv")
    name_filter = make_test_name_filter("Guinness")
    assert not query.get_filtered_inventory(name_filter)


def test_multiple_beers_name_filter_true():
    query = make_test_inventory_query("three.csv")
    name_filter = make_test_name_filter("Bells Best Brown")
    assert len(query.get_filtered_inventory(name_filter)) == 1


def test_multiple_beers_name_filter_false():
    query = make_test_inventory_query("three.csv")
    name_filter = make_test_name_filter("Guinness")
    assert not query.get_filtered_inventory(name_filter)
