#!/usr/bin/env python3
"""Module that defines Shape hierarchy and duck typing inspector."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self):
        """Compute the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Compute the perimeter of the shape."""
        pass


class Circle(Shape):
    """Concrete class representing a circle."""

    def __init__(self, radius):
        """Initialize circle radius."""
        self.radius = radius

    def area(self):
        """Compute circle area."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Compute circle perimeter."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Concrete class representing a rectangle."""

    def __init__(self, width, height):
        """Initialize rectangle dimensions."""
        self.width = width
        self.height = height

    def area(self):
        """Compute rectangle area."""
        return self.width * self.height

    def perimeter(self):
        """Compute rectangle perimeter."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter relying on duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
