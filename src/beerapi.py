import requests
import datetime
import time


import logging

logging.basicConfig(filename= 'test.log',level=logging.INFO,format='%(asctime)s:%(message)s')



def get_beer_data():
    beer_inventory = requests.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv')
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    beer_inventory_file = open(filename, "w+")
    beer_inventory_file.write(beer_inventory.text)


def go():

    while True:
        try:
            get_beer_data()
            logging.info('The data was fetched successfully!')
            time.sleep(1200)
        except:
            logging.exception('Failed to fetch file:')
            time.sleep(1200)
            pass