"""
 This module is for the available inventory
"""


def keep_requested_attributes(beer):
    return {key: beer[key] for key in ['name', 'size', 'category', 'price', 'quantity', ]}


class InventoryQueries:
    """
    This class initiates a Query of Inventory
    """
    def __init__(self, inventory):
        self.inventory = inventory

    def get_available_inventory(self):
        return [keep_requested_attributes(beer) for beer in self.inventory.get_historic_inventory()
                if beer['quantity'] > 0]
