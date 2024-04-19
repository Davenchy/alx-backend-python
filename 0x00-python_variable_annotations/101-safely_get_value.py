#!/usr/bin/env python3
"""This task has again a function that I will add its annotations to satisfy
the next
dct: typing.Mapping
key: typing.Any
default: typing.Union[~T, NoneType]
return: typing.Union[typing.Any, ~T]"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """returns the value mapped to the key in the dct if exist otherwise
    returns the default value if defined else returns None"""
    if key in dct:
        return dct[key]
    else:
        return default
