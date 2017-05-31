#!/usr/bin/python3
"""
Module that saves an object to a text file using JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ saves an object to a text file using JSON representation """
    with open(filename, encoding="UTF-8", mode="w") as a_file:
        a_file.write(json.dumps(my_obj))
