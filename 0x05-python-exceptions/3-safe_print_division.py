#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    finally:
        print("inside result = {}".format(res))
        return res
