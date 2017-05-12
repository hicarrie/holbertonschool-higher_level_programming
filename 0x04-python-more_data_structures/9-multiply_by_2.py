#!/usr/bin/python3
def multiply_by_2(my_dict):
    mul = lambda x: x * 2
    new_dict = {k: mul(v) for k, v in my_dict.items()}
    return new_dict
