#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
    else:
        for i in range(len(matrix)):
            for nums in range(len(matrix[i])):
                if nums != len(matrix[i])-1:
                    last_space = ''
                else:
                    last_space = ""
                print("{:d}".format(matrix[i][nums]), end=last_space)
            print()
