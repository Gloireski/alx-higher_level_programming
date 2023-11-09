#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    list1 = []
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            list1.append(j)
    return list1
