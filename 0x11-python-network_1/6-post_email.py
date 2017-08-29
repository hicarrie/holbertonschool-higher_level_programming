#!/usr/bin/python3
"""
Sends a POST request and email to a URL and displays the body of the response
"""


import sys
import requests


if __name__ == "__main__":
    r = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(r.text)
