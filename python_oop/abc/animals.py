#!/usr/bin/env python3
"""Module that defines an abstract Animal class and its subclasses."""
from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Concrete class representing a dog."""

    def sound(self):
        """Return the bark sound."""
        return "Bark"


class Cat(Animal):
    """Concrete class representing a cat."""

    def sound(self):
        """Return the meow sound."""
        return "Meow"
