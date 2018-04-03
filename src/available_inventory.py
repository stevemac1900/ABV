from beer import Beer
def make_subset(item):
    return {key: item[key] for key in ['name', 'size', 'category', 'price', 'quantity']}

def make_beer(item):
    # we are substituting style for category for now
    return Beer(item['name'], item['size'], item['category'], item['price'], item['quantity'])
class InventoryQueries:

    def __init__(self, inventory):
        self.inventory = inventory

    def get_available_inventory(self):
        return [make_subset(item) for item in self.inventory.get_historic_inventory() if item['quantity'] > 0]

    def get_filtered_inventory(self, filter):
        return [make_beer(item) for item in self.inventory.get_historic_inventory() if filter.is_match(make_beer(item))]
