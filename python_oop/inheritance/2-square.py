#!/usr/bin/env python3
"""A module defining an extended square subclass."""
SquareBase = __import__('1-square').Square


class Square(SquareBase):
    """Represents a square shape with custom print format."""

    def __str__(self):
        """Return the square description."""
        width = self._Rectangle__width
        height = self._Rectangle__height
        return "[Square] {}/{}".format(width, height)
