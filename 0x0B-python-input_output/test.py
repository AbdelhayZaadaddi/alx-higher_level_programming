#!/usr/bin/python3
"""read_file module.

Containes a function that reads a text file.
"""

def append_write(filename="", text=""):
    with open(filename, 'a') as f:
        return f.write(text)