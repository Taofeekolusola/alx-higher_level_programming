#!/usr/bin/python3
"""Defines file-writing function"""

def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)

    Args:
        filename (str) - the name of the file to write
        text (str) - the text to write

    Returns:
        the number of characters written
        
    """
    with open(filename "w", encoding="utf-8") as fn:
        return fn.write(text)
