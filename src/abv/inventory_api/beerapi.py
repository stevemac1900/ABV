import json
from flask import Flask, request
from abv.inventory_api.current_inventory import Inventory
from abv.inventory_api.inventory_queries import InventoryQueries
from abv.inventory_api.filter_ds import FilterDS
from abv.inventory_api import style_db, most_recent_file
from abv.inventory_api.file_location import FileLocation


APP = Flask(__name__)
queries = None


def initialize_inventory():
    location = FileLocation.save_location
    the_file = most_recent_file.MostRecentFile(location)
    style = style_db.StyleDB()
    inventory = Inventory(the_file, style)
    global queries
    queries = InventoryQueries(inventory)


@APP.route('/current')
def get_current_inventory():
    keys = list(request.args.keys())
    for key in keys:
        if key != 'name' and key != 'size' and key != 'style' and key != 'availability':
            return "Bad parameter given!", 400

    name = request.args.get('name')
    size = request.args.get('size')
    style = request.args.get('style')
    availability = request.args.get('availability')

    beer_filter = FilterDS(name=name, size=size, style=style, availability=availability)
    beers = []
    filtered_inventory = queries.get_filtered_inventory(beer_filter)
    if filtered_inventory:
        for beer in filtered_inventory:
            beers.append({'name': beer.name, 'size': beer.size, 'style': beer.style,
                          'quantity': beer.quantity, 'price': beer.price})
        return json.dumps(beers)
    return json.dumps([])


if __name__ == "__main__":
    initialize_inventory()
    APP.run(host="0.0.0.0")
