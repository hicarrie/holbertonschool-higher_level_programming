#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    sorted(my_dict)
    for k, v in my_dict.items():
        print("{}: {}".format(k, v))
