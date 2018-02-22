import requests
import datetime
import time

def get_beer_data():
    beer_inventory = requests.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv')
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    beer_inventory_file = open(filename, "w+")
    beer_inventory_file.write(beer_inventory.text)
    time.sleep(3600)

while True:
    try:
        get_beer_data()
        time.sleep(3600)
    except:
        time.sleep(3600)
        continue