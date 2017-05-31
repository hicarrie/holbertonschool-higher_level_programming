#!/usr/bin/python3
"""
Module for returning number of lines in text file
"""


def number_of_lines(filename=""):
    """ returns number of lines in file """
    counter = 0
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            counter = counter + 1
    return counter
