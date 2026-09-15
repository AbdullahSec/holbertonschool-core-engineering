# Python - Hello, World

## Description
This project marks the transition from low-level systems programming in C to high-level programming in Python. It focuses on understanding the internal mechanics of the Python interpreter, execution modes (interactive vs. script), variable interpolation, output formatting, and standard styling guidelines under PEP 8.

## Requirements
* Operating System: Ubuntu 20.04 LTS or newer
* Python Version: Python 3.8+ (executed via `python3`)
* Style Guide: All scripts must adhere to `pycodestyle` (PEP 8 standard)
* Execution: All script files must be executable and start with `#!/usr/bin/python3`

## Environment Setup
It is recommended to run all scripts inside a Python virtual environment:

```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install style checker
pip install pycodestyle