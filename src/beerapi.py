import requests
import datetime
import time

def get_beer_data():
    """
    Retrieves inventory data from Tanczos and saves data locally

    Input:
        Parameterless

    Output:
        Returns void and writes a csv file locally
    """
    beer_inventory = requests.get('http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv')
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    beer_inventory_file = open(filename, "w+")
    beer_inventory_file.write(beer_inventory.text)

while True:
    try:
        get_beer_data()
    except:
        pass

    time.sleep(3600)