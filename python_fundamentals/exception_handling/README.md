# Python - Exception Handling

## Description
This project focuses on handling errors and exceptions defensively and predictably in Python. It covers the mechanics of runtime exceptions, the `try`, `except`, `else`, and `finally` control structures, raising custom exceptions, and adhering to strict Python coding standards.

## Requirements
* OS: Ubuntu 20.04 LTS
* Python Version: Python 3.8.x
* Coding Style: PEP 8 compliant (`pycodestyle 2.7.*`)
* All script files must be executable (`chmod u+x <filename>`)
* All files must begin with `#!/usr/bin/env python3`
* All files must end with a new line

## Learning Objectives
* Understand why Python uses exception handling instead of silent failures.
* Distinguish common built-in exceptions (`TypeError`, `ValueError`, `ZeroDivisionError`, `IndexError`).
* Avoid bare `except:` clauses by targeting specific exceptions.
* Correctly apply `else` and `finally` execution paths.
* Raise exceptions deliberately using `raise`.

## Tasks

| File | Description | Prototype |
|---|---|---|
| `safe_print_list.py` | Prints `x` elements of a list safely without using `len()` | `def safe_print_list(my_list=[], x=0):` |

## Author
* Abdullah