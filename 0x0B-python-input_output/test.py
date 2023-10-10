#!/usr/bin/python3
"""read_file module.

Containes a function that reads a text file.
"""


def read_file(filename=""):
    with open(filename, 'r') as f:
        print(f.read(), end)