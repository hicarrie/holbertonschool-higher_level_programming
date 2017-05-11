#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    if my_dict is None or len(my_dict) == 0:
        print()
        return
    sorted(my_dict)
    for k, v in my_dict.items():
        print("{}: {}".format(k, v))
