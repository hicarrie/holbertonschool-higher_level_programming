#!/usr/bin/python3
"""
Module for function that reads lines of a text file
"""


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file and prints to stdout """
    line_count = number_of_lines(filename)
    if nb_lines >= line_count or nb_lines <= 0:
        nb_lines = line_count

    with open(filename, encoding="utf-8") as a_file:
        for i in range(nb_lines):
            print("{}".format(a_file.readline()), end="")


def number_of_lines(filename=""):
    """ returns number of lines in file """
    counter = 0
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            counter = counter + 1
    return counter
