#!/usr/bin/python3
# 0-read_file.py
# Belem Gloire BEKOUTOU
"""define read_file fn"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:

    Args:
        filename: file to read
    """
    with open(filename, encoding="utf-8") as f:
        read_f = f.read()
        print(read_f)
