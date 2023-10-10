#!/usr/bin/env python3
"""
0: async generator
"""
import random
import asyncio


async def async_generator() -> float:
    """loops 10 times returning a random float per second"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
