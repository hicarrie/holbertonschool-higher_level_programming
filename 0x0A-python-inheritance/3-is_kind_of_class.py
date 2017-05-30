#!/usr/bin/python3
"""
Module that checks if an object is an instance of the specified class or
if the object is an instance of a class inherited from the specified class
"""


def is_kind_of_class(obj, a_class):
    """ Returns true if object is an instance of a class or class inherited
    from the class """
    if isinstance(obj, a_class):
        return True
    else:
        return False
