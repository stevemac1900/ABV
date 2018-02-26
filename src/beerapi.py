import requests
import datetime
import time
import logging
logging.basicConfig(filename='connection.log',level=logging.DEBUG)

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


    except requests.exceptions.ConnectionError as err:
        error = str(err).split(':')
        arrayLen = len(error)
        error_msg = format(type(err).__name__) + " " + error[arrayLen - 2][1:] + ":" + error[arrayLen - 1][:-4] + ")"
        logging.warning(error_msg)
        time.sleep(3600)
