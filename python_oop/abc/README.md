# Python - Object-Oriented Programming: Abstract Classes, Mixins, and Duck Typing

## Description
This project covers advanced Object-Oriented Programming (OOP) patterns in Python, including:
- Abstract Base Classes (ABC) and abstract methods
- Interfaces and duck typing
- Multiple inheritance and Method Resolution Order (MRO)
- Mixins for modular behavioral composition
- Extending built-in standard library classes

## Requirements
- OS: Ubuntu 20.04 LTS
- Python version: Python 3.8.x
- Style guidelines: PEP 8 (`pycodestyle` version 2.7.*)
- All files are executable and end with a newline
- Fully documented modules, classes, and methods

## Files Overview
| File | Description |
| --- | --- |
| `animals.py` | Abstract `Animal` class with `sound()` and concrete `Dog` and `Cat` classes. |
| `shapes.py` | Abstract `Shape` class, `Circle`, `Rectangle`, and `shape_info()` duck typing function. |
| `flyingfish.py` | `FlyingFish` class illustrating multiple inheritance from `Fish` and `Bird`. |
| `dragon.py` | `Dragon` class combining `SwimMixin` and `FlyMixin`. |
| `verboselist.py` | `VerboseList` subclassing built-in `list` with mutation notifications. |
