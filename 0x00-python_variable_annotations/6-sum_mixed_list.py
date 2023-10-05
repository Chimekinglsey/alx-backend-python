#!/usr/bin/env python3
"""
6. Complex types - mixed list
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Takes an input list of float and returns their sum"""
    sum: List[float] = 0
    for num in mxd_lst:
        sum += num
    return sum


"""Newer versions of python 3.9+ doesn't need any"""
"""of these imports. sum: list[float] will work seamlessly"""
