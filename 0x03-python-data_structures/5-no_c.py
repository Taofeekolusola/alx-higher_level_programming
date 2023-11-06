#!/usr/bin/env python3
def no_c(my_string):
    letter_to_remove = 'c'
    new_string = ""
    for char in my_string:
        if char != letter_to_remove:
            new_string += char
    print(new_string)
