#!/usr/bin/python3
# 2-append_write.py
# Belem Gloire BEKOUTOU
"""define append fn"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file (UTF8)
    and returns the number of characters added:

    Args:
        filename: file to append data to
        text: to to append

    Return: nb of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        nb = f.write(text)
        return nb
