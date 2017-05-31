#!/usr/bin/python3
"""
Module that appends a string at the end of a UTF-8 text file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ appends a string to the end of text file and returns
    number of characters added """
    with open(filename, encoding="UTF-8", mode="a") as a_file:
        return a_file.write(text)
