#!/usr/bin/env python3
"""
 101. More involved type annotations
"""
from typing import TypeVar, Union, Any, Mapping

T = TypeVar('T')
R = Union[Any, T]
Df = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default=Df) -> R:
    """More annotation """
    if key in dct:
        return dct[key]
    else:
        return default
