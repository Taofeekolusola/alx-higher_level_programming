#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    Max = 0
    for key, v in a_dictionary.items():
        if v > Max:
            Max = v
    for key, v in a_dictionary.items():
        if v == Max:
            return key
