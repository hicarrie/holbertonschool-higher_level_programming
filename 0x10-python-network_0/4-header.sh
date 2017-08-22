#!/bin/bash
# Sends a GET request and displays body of the response
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
