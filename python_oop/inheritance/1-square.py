#!/usr/bin/env python3
"""A module defining a square subclass."""
Rectangle = __import__('1-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size):
        """Initialize square size.

        Args:
            size (int): Square size.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Compute the square area."""
        return self.__size ** 2
