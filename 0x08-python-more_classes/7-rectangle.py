#!/usr/bin/python3
"""Rectangle module.

This module contains a class that defines a rectangle.

"""


class Rectangle:
    """A class that defines a rectangle.

    Attributes:
        number_of_instances (int): A class attribute to keep track of the number of instances created.
        print_symbol: A class attribute used as a symbol for string representation.

    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize a Rectangle instance with optional width and height.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.

        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get or set the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation.

        Args:
            value (int): The width value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get or set the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation.

        Args:
            value (int): The height value to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return a string representation of the rectangle.

        Returns:
            str: A string representing the rectangle using the print_symbol.

        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([str(self.print_symbol) * self.__width] * self.__height)

    def __repr__(self):
        """Return a string representation of the rectangle for recreation.

        Returns:
            str: A string representation that can be used with eval() to recreate the instance.

        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Delete a rectangle instance and decrement the number_of_instances attribute."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
