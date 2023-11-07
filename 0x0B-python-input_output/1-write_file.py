#!/usr/bin/python3
# 0-read_file.py
# Belem Gloire BEKOUTOU
"""define write_file fn"""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8) and
    returns the number of characters written:

    Args:
        filename: file to write
        text: text to write
    Return: number of char written
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        nb = f.write(text)
        return nb
