import requests
import datetime
import time
import logging

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



def go():
    """
    Fetches beer data every 20 minutes

    Input:
        Parameterless

    Output:
        Returns void

    Raises:
        Exception
            When unable to fetch file, logs error and passes
    """
    while True:
        try:
            get_beer_data()
            logging.info('The data was fetched successfully!')
            time.sleep(1200)
        except:
            logging.exception('Failed to fetch file:')
            time.sleep(1200)
            pass

if __name__ == "__main__":
    logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s:%(message)s')
    go()

