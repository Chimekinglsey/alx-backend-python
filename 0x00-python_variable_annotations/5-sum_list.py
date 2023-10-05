#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes an input list of float and returns their sum"""
    sum: List[float] = 0
    for num in input_list:
        sum += num
    return sum


"""Newer versions of python 3.9+ doesn't need any"""
"""of these imports. sum: list[float] will work seamlessly"""
