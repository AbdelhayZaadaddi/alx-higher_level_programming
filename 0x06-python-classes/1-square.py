#!/usr/bin/python3
"""Square module.

This module contains a class that defines a square and int method

"""


class Square():
    """Defines a square."""

    def __init__(self, size):
        """Sets the necessary attributes for the square object
        
        Args:
            size (int): the size of one edge of the square.
        """
        self.__size = size
