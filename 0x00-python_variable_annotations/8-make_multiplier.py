#!/usr/bin/env python3
"""This task contains a complex annotated function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes an argument as a float and returns a function that
    takes another float and returns the multiplication of both floats as a
    float"""

    def multiplier_call(x: float):
        return x * multiplier

    return multiplier_call
