import csv


def convert_to_numeric(item):
    result = dict(item)
    result['name'] = result['name'].title()
    result['size'] = result['size'].title()
    result['category'] = result['category'].title()
    result['quantity'] = float(result['quantity'])
    result['price'] = float(result['price'])
    result['case_price'] = float(result['case_price'])
    result['case_pack'] = float(result['case_pack'])
    return result


class Inventory:
    def __init__(self, filename):
        with open(filename) as csvfile:
            reader = csv.DictReader(csvfile,
                                    fieldnames=('name', 'size', 'category', 'quantity',
                                                'price', 'case_price', 'case_pack'))

            self.inventory = [convert_to_numeric(item) for item in reader]

    def get_historic_inventory(self):
        return self.inventory
