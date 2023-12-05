#!/usr/bin/python3
"""Defines a text file that reads function."""


def read_file(filename=""):
    """Prints the contents of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as fn:
        print(fn.read(), end="")
