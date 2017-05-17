#!/usr/bin/python3
"""
Module that prints a square with the character #
"""


def print_square(size):
    """
    Function that prints a square of size with the character #
    """

    """Checks if size is an integer"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    """Checks if size is negative"""
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
