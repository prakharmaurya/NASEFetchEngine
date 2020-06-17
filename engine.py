from mapLinksConsts import LINKS
from utils.link_assambler import assamble
import time
from utils.fetcher_dir.fetcher import fetch
from utils.filter import filter
import json
import pymongo
from configparser import ConfigParser
import urllib
config = ConfigParser()


def mainLoop():
    try:
        config.read('./config.ini')
    except:
        print('config file not found')
        return

    try:
        client = pymongo.MongoClient(
            "mongodb+srv://"+urllib.parse.quote(config.get('DATABASE', 'DB_USERNAME'))+":"+urllib.parse.quote(config.get('DATABASE', 'DB_PASSWORD'))+"@cluster0-txzvy.mongodb.net/?retryWrites=true&w=majority")
        op_chainDB = client[config.get('DATABASE', 'DB_NAME')]
        print('Connected to DB')
    except:
        print('Data base Connection Failed')
        return

    try:
        links = assamble(LINKS)
    except:
        print('Link constant file error')
        return

    while(True):

        try:
            print('Data fetch started')
            fetch(links)
        except:
            print('Data fetch failed')

        try:
            with open('response_data.json', 'r') as f:
                file_data = json.load(f)
        except:
            print('Response read failed')

        try:
            print("Filtering stated")
            for link in links:
                symbol = link.split('=')[1]
                if(file_data.get(symbol)):
                    filter(op_chainDB, symbol, file_data[symbol])

            print("Data written to DB")
        except:
            print("Filtering is not satisfied with data")
        print('sleeping for '+config.get('FETCH', 'TIME_TO_DATA_FETCH')+"s")
        time.sleep(int(config.get('FETCH', 'TIME_TO_DATA_FETCH')))
