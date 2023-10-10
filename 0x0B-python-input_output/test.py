#!/usr/bin/python3
"""read_file module.

Containes a function that reads a text file.
"""


def write_file(filename="", text=""):
    with open(filename, 'w') as f:
        return f.write(text)