#!/usr/bin/env python3
"""In this task I should use mypy to fix the code typing"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """returns a list which contains the values of lst repeated factory times
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
