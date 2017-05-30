#!/usr/bin/python3
"""
Module that checks if an object is exactly an instance of a class
"""


def is_same_class(obj, a_class):
    """ Returns True if an object is exactly an instance of the specified
    class, otherwise returns False """
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
