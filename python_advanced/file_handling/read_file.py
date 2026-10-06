#!/usr/bin/env python3

"""Read and print the contents of a UTF-8 text file."""

def read_file(filename=""):
    with open(file, encoding="utf-8")as file:
        print(file.read(), end="")
