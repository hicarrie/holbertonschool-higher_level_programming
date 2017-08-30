#!/usr/bin/python3
"""
Sends a POST request to a URL and displays the body of the response
"""


import sys
import urllib.request


if __name__ == "__main__":
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf8'))
