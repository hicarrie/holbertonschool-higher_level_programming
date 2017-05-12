#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    if len(my_dict) == 0:
        return sorted(my_dict, key=lambda score: score[2])[0]
    else:
        return sorted(my_dict, key=lambda score: score[2])[-1]
