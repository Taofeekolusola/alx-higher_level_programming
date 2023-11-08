#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    j = 0
    k = 0

    for i in my_list:
        j += i[0] * i[1]
        k += i[1]

    return (j / k)
