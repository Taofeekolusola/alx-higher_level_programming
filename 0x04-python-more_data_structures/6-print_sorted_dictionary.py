#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a = sorted(a_dictionary)
    for b in a:
        print("{}: {}".format(b, a_dictionary[b]))
