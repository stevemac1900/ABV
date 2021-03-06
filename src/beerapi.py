import requests
import datetime
import time
import logging


def write_beer_inventory():
    """
    Retrieves inventory data from Tanczos and writes to file locally
    """
    beer_inventory = get_inventory()
    if beer_inventory is not "":
        write_inventory(beer_inventory)


def write_inventory(beer_inventory):
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    try:
        with open(filename, "w+") as beer_inventory_file:
            beer_inventory_file.write(beer_inventory)
        logging.info('The data was fetched successfully!')
    except OSError as e:
        error_subclass = type(e).__name__
        logging.exception('Failed to fetch file: {}'.format(error_subclass))
        pass


def get_inventory():
    """

    Returns: The inventory or an emtpy string if the communication failed.

    """
    try:
        beer_inventory = requests.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv')
        return beer_inventory.text
    except requests.exceptions.ConnectionError as e:
        error_subclass = type(e).__name__
        logging.exception('Failed to fetch file: {}'.format(error_subclass))
        return ""

def run():
    """
    Runs write_beer_inventory every 20 minutes

    Input:
        None

    Output:
        Returns void
    """
    seconds_between_fetches = 1200

    while True:
        write_beer_inventory()
        time.sleep(seconds_between_fetches)


if __name__ == "__main__":
    logging.basicConfig(filename='abv.log', level=logging.INFO, format='%(asctime)s:%(message)s')
    run()
