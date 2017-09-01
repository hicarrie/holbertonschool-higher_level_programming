#!/usr/bin/python3
# Sends a search request to the Star Wars API

import sys
import requests


if __name__ == "__main__":
    url = 'https://api.github.com/user/'
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=(user, pwd))
    print(r_json.get('id'))
