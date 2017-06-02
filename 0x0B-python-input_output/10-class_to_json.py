#!/usr/bin/python3
"""
Module that returns the dictionary description with simple data
structure for JSON serialization of an object
"""


import json


def class_to_json(obj):
    """ function that returns dictionary description with simple
    data structure for JSON serialization of an object """
    json_obj = json.dumps(obj.__dict__)
    return json.loads(json_obj)
