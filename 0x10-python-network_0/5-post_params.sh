#!/bin/bash
# Sends a GET request and displays body of the response
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I%20will%20always%20be%20here%20for%20PLD"
