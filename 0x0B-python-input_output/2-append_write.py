#!/usr/bin/python3
"""Defines a file that appends function."""


def write_file(filename="", text=""):
    """Appends a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The text to be appended to the file.
    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as fn:
        return fn.write(text)
