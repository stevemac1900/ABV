from available_inventory import InventoryQueries
from inventory import Inventory
from name_filter import NameFilter
from yes_filter import YesFilter

def test_one_beer_true():
    inventory = Inventory("sample_csv_files/single.csv")
    yes_filter = YesFilter()
    name_filter =  NameFilter(yes_filter, "Bells Best Brown")
    query = InventoryQueries(inventory)
    assert query.get_available_inventory(name_filter) == True