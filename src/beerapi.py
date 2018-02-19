import datetime
import requests
import time

def get_beer_data():
    result = requests.get("http://www.tanczos.com/tanczos.com/beerinventory/webexport.csv")
    filename = str(datetime.datetime.now()).replace(' ', '_') + '.csv'
    with open(filename, "w") as outfile:
        for line in result.text:
            outfile.write(line)

while True:
    try:
        get_beer_data()
        time.sleep(3600)
        print("waiting...")
    except:
        print("WHOOPSIE")
        time.sleep(3600)
        continue
