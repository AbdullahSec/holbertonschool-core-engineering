#!/usr/bin/env python3
"""A module demonstrating inheritance and polymorphism."""


class Animal:
    """Represents a base animal."""

    def speak(self):
        """Return the animal voice sound."""
        return "Some sound"


class Dog(Animal):
    """Represents a dog subclass."""

    def speak(self):
        """Return dog bark."""
        return "Woof"


class Cat(Animal):
    """Represents a cat subclass."""

    def speak(self):
        """Return cat meow."""
        return "Meow"


if __name__ == "__main__":
    animals = [Dog(), Cat(), Dog()]
    for animal in animals:
        print(animal.speak())

    dog = Dog()
    print(isinstance(dog, Dog))
    print(isinstance(dog, Animal))
    print(issubclass(Dog, Animal))
