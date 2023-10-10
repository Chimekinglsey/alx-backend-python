#!/usr/bin/env python3
"""
0. Async Generator
"""
import random
import asyncio
from typing import Iterator


async def async_generator():
    """loops  10 times yielding a random num after 1 sec"""
    for _ in range(10):
        value = random.uniform(0, 10)
        yield value
        await asyncio.sleep(1)
