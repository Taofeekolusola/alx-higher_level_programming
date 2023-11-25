#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """Adds two integers.

    Args:
        a: the first integer to be added.
        b: the second integer, set at default 98.

    Raises:
        TypeError: if a, b are not int, float.

    Returns:
        The sum of the two integers."""

    if type(a) not in (float, int):
        raise TypeError('a must be an integer')
    if type(b) not in (float, int):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
