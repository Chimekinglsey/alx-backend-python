#!/usr/bin/env python3
"""
1: async comprehensions
"""
from typing import List
gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collects random numbers from gen() and returns it"""
    return [i async for i in gen()]
