#!/usr/bin/python3
def roman_to_int(roman_string: str):
    if roman_string is None or type(roman_string) != str:
        return 0
    items = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = [items[a] for a in roman_string] + [0]
    counter = 0

    for b in range(len(num) - 1):
        if numb[b] >= num[b+1]:
            counter += num[b]
        else:
            counter -= numbers[b]

    return counter
