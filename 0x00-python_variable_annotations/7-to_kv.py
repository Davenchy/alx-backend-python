#!/usr/bin/env python3
"""This task contains an annotated function that takes k and v and returns
a tuple of k and v squared"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple of k and v squared"""
    return (k, v**2)
