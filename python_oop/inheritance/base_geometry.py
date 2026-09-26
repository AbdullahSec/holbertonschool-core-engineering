#!/usr/bin/env python3
"""A module defining a base geometry class."""


class BaseGeometry:
    """Represents base geometry shapes."""

    def area(self):
        """Compute the shape area.

        Raises:
            Exception: Calculation is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate an integer value.

        Args:
            name (str): The parameter name.
            value (int): The parameter value.

        Raises:
            TypeError: When value is not an integer.
            ValueError: When value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
