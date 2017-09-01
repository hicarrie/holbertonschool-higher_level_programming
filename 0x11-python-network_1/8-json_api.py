#!/usr/bin/python3
# Sends a request to a URL and displays the body of the response

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) < 2:
        payload = {'q': ''}
    else:
        payload = {'q': sys.argv[1]}

    r = requests.post('http://0.0.0.0:5000/search_user', data=payload)

    r_json = r.json()

    if r.headers['content-type'] is 'application/json':
        print("Not a valid JSON")
    elif len(r_json) == 0:
        print("No result")
    else:
        print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
