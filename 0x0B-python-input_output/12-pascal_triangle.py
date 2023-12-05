#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represents Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triang = [[1]]
    while len(triang) != n:
        tri = triang[-1]
        swap = [1]
        for a in range(len(tri) - 1):
            swap.append(tri[a] + tri[a + 1])
        swap.append(1)
        triang.append(swap)
    return triang
