#!/usr/bin/python3
"""
This is the print_square module.

This module supplies one function, print_square().
"""


def print_square(size):
    """
    Prinnt a square with the character #

    Args:
        size (int): the size lenght of the square.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must ne >= 0")
    
    print(("#" * size + '\n') * size, end="")
