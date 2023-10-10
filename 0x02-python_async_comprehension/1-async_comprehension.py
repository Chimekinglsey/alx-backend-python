#!/usr/bin/env python3
"""
1: async comprehensions
"""
gen = __import__('0-async_generator').async_generator


async def async_comprehension() -> float:
    """collects random numbers from gen and return it"""
    return [i async for i in gen()]
