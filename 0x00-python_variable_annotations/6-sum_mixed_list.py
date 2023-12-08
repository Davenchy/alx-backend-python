#!/usr/bin/env python3
"""This task has a function that takes a list of mixed arguments
floats and integers and returns their sum as a float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """returns the sum of a list of floats and integers"""
    return sum(mxd_lst)
