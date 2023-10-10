#!/usr/bin/env python3
"""
0: async generator
"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """loops 10 times returning a random float per second"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
