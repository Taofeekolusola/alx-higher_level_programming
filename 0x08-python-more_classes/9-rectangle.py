#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle.

    Attributes:
        number_of_instances (int): The number of Rectangle instances.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Begins a new Rectangle.

        Args:
            width (int): The width of the new rectangle.
            height (int): The height of the new rectangle.
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get and set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get and set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    @staticmethod
    def bigger_or_equal(rectang_1, rectang_2):
        """Returns the Rectangle with the greater area.

        Args:
            rectang_1 (Rectangle): The first Rectangle.
            rectang_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rectang_1 or rectang_2 is not a Rectangle.
        """
        if not isinstance(rectang_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rectang_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rectang_1.area() >= rectang_2.area():
            return (rectang_1)
        return (rectang_2)

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle with width and height equal to size.

        Args:
            size (int): The width and height of the new Rectangle.
        """
        return (cls(size, size))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        rectang = []
        for a in range(self.__height):
            [rectang.append(str(self.print_symbol)) for b in range(self.__width)]
            if a != self.__height - 1:
                rectang.append("\n")
        return ("".join(rectang))

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        rectang = "Rectangle(" + str(self.__width)
        rectang += ", " + str(self.__height) + ")"
        return (rectang)

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
