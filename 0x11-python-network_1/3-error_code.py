#!/usr/bin/python3
# Sends a request to a URL and displays the body of the response

import sys
import urllib.request


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf8'))
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
