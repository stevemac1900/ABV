import requests
import datetime
import time

def write_beer_inventory():
    beer_inventory = requests.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv')
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    with open(filename, "w+") as beer_inventory_file:
        beer_inventory_file.write(beer_inventory.text)


def run():
    while True:
        try:
            write_beer_inventory()
        except:
            pass
        time.sleep(1200)

if __name__ == "__main__":
    run()
