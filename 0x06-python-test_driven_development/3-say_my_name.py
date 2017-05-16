#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    prints "My name is" followed by first name and last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if first_name == None:
        first_name == ""
    if last_name == None:
        last_name == ""
    print("My name is {} {}".format(first_name, last_name))
