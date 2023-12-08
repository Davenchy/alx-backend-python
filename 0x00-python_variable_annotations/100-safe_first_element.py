#!/usr/bin/env python3
"""Again in this task I will write function annotations to give be the same as
{
    'lst': typing.Sequence[typing.Any],
    'return': typing.Union[typing.Any, NoneType]
}"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """this function returns the first element of a sequence object if any was
    passed or None if nothing was passed"""
    if lst:
        return lst[0]
    else:
        return None
