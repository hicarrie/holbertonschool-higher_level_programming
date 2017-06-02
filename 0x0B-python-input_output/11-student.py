#!/usr/bin/python3
"""
Defines class Student
"""


import json


class Student:
    """ initializes instance """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ function that returns dictionary description with simple
        data structure for JSON serialization of an object """
        json_obj = json.dumps(self.__dict__)
        return json.loads(json_obj)
