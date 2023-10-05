#!/usr/bin/env python3
"""
8. Complex types - multiplier
"""
from typing import Union, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float"""

    def mul_func(num: float) -> float:
        """multiplier function"""
        return num * multiplier

    return mul_func


"""Newer versions of python 3.9+ doesn't need any"""
"""of these imports. `v: int | float` will work seamlessly"""
