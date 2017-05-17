#!/usr/bin/python3
"""
Module that prints "My name is" followed by first name and last name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is followed by first_name and last_name
    """

    """Checks that variables are strings"""
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    """Sets None variables to empty strings"""
    if first_name is None:
        first_name == ""
    if last_name is None:
        last_name == ""

    print("My name is {} {}".format(first_name, last_name))
