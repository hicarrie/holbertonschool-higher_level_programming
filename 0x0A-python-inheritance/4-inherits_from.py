#!/usr/bin/python3
"""
Module that checks if an object is an instance of a class inherited
from the specified class
"""


def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and not issubclass(a_class, type(obj)):
        return True
    else:
        return False
