from abv.inventory_api.beer import Beer


class Inventory:
    def __init__(self, tanczos_inventory, style_db):

        self.inventory = []

        # tanczos_inventory = MostRecentFile().get_list()
        # style_db = MockBreweryDBStoutTracked()

        for beer in tanczos_inventory:
            style = style_db.get_style(beer[0])
            full_beer = Beer(beer[0], beer[1], style, beer[3], beer[4])
            self.inventory.append(full_beer)

    def get_historic_inventory(self):
        return self.inventory
