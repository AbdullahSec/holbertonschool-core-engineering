#!/usr/bin/env python3
def pow(a, b):
    if b < 0:
        return 1 / pow(a, -b)
    res = 1
    for _ in range(b):
        res *= a
    return res
