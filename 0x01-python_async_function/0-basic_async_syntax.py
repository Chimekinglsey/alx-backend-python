#!/usr/bin/env python3
"""
0. The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """returns a random from in the range of 0 and `max_delay` """
    value = random.uniform(0, max_delay)
    await asyncio.sleep(value)
    return value
