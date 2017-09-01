#!/usr/bin/python3
# Sends a search request to the Star Wars API

import sys
import requests


if __name__ == "__main__":
    r = requests.get('https://swapi.co/api/people/?search=' + sys.argv[1])
    r = r.json()
    print("Number of results: {}".format(r.get('count')))
    for name in r.get('results'):
        print(name['name'])
