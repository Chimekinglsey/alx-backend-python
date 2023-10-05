#!/usr/bin/env python3
"""
7. Complex types - string and int/float to tuple
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Takes k,v returns the square of v"""
    return (k, v**2)


"""Newer versions of python 3.9+ doesn't need any"""
"""of these imports. `v: int | float` will work seamlessly"""
