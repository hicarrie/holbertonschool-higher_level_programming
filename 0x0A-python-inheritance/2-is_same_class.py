#!/usr/bin/python3
"""
Returns True if an object is exactly an instance of the specified
class, otherwise returns False
"""

def is_same_class(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is a_class:
        return True
    else:
        return False
