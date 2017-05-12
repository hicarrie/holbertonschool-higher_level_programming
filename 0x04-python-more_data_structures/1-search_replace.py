#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return
    new_list = []
    change = lambda match: True if x == search else False
    for x in my_list:
        if change(x) is True:
            new_list.append(replace)
        else:
            new_list.append(x)
    return new_list
