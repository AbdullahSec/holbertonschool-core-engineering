# Python - Inheritance and Polymorphism

## Description
This project focuses on Object-Oriented Programming (OOP) concepts in Python, specifically inheritance, method overriding, and polymorphism. It demonstrates how subclasses extend parent classes, reuse validation methods, and implement specialized behaviors.

## Requirements
- OS: Ubuntu 20.04 LTS
- Python: version 3.8.x
- Style: `pycodestyle` (version 2.7.*)
- All files are executable and end with a newline
- Full docstrings for modules, classes, and methods

## Files Overview
| File | Description |
| --- | --- |
| `0-polymorphism_demo.py` | Demonstration script for class inheritance and polymorphism. |
| `base_geometry.py` | `BaseGeometry` class with `area()` exception and `integer_validator()`. |
| `1-rectangle.py` | `Rectangle` class inheriting from `BaseGeometry` with private attributes. |
| `1-square.py` | `Square` class inheriting from `Rectangle` with size validation and `area()`. |
| `2-square.py` | `Square` class with overridden `__str__()` representation `[Square] <width>/<height>`. |
