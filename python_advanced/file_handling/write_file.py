#!/usr/bin/env python3

"""Write a string to a UTF-8 text file and return
the number of characters written."""


def write_file(filename="", text=""):
    '''____'''
    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        return
