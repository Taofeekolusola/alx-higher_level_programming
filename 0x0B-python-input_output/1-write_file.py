#!/usr/bin/python3
"""Defines a file that writes function."""


def write_file(filename="", text=""):
    """Writes a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as fn:
        return fn.write(text)
