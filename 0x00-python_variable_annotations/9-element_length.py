#!/usr/bin/env python3
"""In this task I got a function and wrote its annotations to be suitable with
the output of the example console"""
from typing import List, Tuple, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function takes a list of any sequence object and returns a list of
    tuples contains the sequence itself and its length"""
    return [(i, len(i)) for i in lst]
