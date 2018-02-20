#Clean Code rename
import requests
import datetime
import time

while True:
    beer_inventory = requests.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv')
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    beer_inventory_file = open(filename, "w+")
    beer_inventory_file.write(beer_inventory.text)
    time.sleep(3600)
