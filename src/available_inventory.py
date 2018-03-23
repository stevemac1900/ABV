
def make_subset(item):
    return {key: item[key] for key in ['name', 'size', 'style', 'price', 'quantity']}


class InventoryQueries:

    def __init__(self, inventory):
        self.inventory = inventory

    def get_filtered_inventory(self, filter):
        return [make_subset(item) for item in self.inventory.get_historic_inventory() if filter.is_match(item)]
