#!/usr/bin/python3
"""
Module that checks if an object is an instance of a class inherited
from the specified class
"""


def inherits_from(obj, a_class):
    """ returns True if obj is an instance of a_class or a class inherited
    from a_class"""
    return isinstance(obj, a_class) and not issubclass(a_class, type(obj))
