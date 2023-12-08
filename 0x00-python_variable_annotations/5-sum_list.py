#!/usr/bin/env python3
"""This task contains a function that returns the sum of a list of floats"""
from functools import reduce


def sum_list(input_list: list[float]) -> float:
    """returns the sum of a list of floats"""
    return reduce(lambda x, y: x + y, input_list, 0)
