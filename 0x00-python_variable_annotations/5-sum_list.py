#!/usr/bin/env python3
"""
5. Complex types - list of floats
"""


def sum_list(input_list: list[float]) -> float:
    """Takes an input list of float and returns their sum"""
    sum: float = 0
    for num in input_list:
        sum += num
    return sum
