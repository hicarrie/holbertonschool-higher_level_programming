#!/usr/bin/python3
def multiply_by_2(my_dict):
    new_dict = {k: v * 2 for k, v in my_dict.items()}
    return new_dict
