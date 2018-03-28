from available_inventory import InventoryQueries
from inventory import Inventory
from name_filter import NameFilter
from yes_filter import YesFilter

base_dir = "tests/sample_csv_files/"
def test_one_beer_name_filter_true():
    inventory = Inventory(base_dir + "single_positive_quantity.csv")
    name_filter =  NameFilter(YesFilter(), "Bells Best Brown")
    query = InventoryQueries(inventory)
    assert query.get_filtered_inventory(name_filter)[0].get_name() == "Bells Best Brown"

def test_one_beer_name_filter_false():
    inventory = Inventory(base_dir + "single_positive_quantity.csv")
    name_filter =  NameFilter(YesFilter(), "Guinness")
    query = InventoryQueries(inventory)
    assert len(query.get_filtered_inventory(name_filter)) == 0

def test_multiple_beers_name_filter_true():
    inventory = Inventory(base_dir + "three.csv")
    name_filter =  NameFilter(YesFilter(), "Bells Best Brown")
    query = InventoryQueries(inventory)
    assert len(query.get_filtered_inventory(name_filter)) == 1

def test_multiple_beers_name_filter_false():
    inventory = Inventory(base_dir + "three.csv")
    name_filter =  NameFilter(YesFilter(), "Guinness")
    query = InventoryQueries(inventory)
    assert len(query.get_filtered_inventory(name_filter)) == 0