#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = list(my_list)
    for a in range(len(my_list)):
        if new_list[a] == search:
            new_list[a] = replace
    return new_list
