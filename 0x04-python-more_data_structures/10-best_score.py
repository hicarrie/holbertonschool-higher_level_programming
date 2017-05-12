#!/usr/bin/python3
def best_score(my_dict):
    if my_dict is None:
        return None
    return sorted(my_dict, key=lambda score: score[2])[-1]
