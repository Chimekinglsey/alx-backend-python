#!/usr/bin/env python3
"""
2. Run time for four parallel comprehensions
"""
import asyncio
import time
as_comp = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measures the runtime of async_comprehension"""
    start_time = time.perf_counter()
    await asyncio.gather(*(as_comp() for _ in range(4)))
    stop_time = time.perf_counter() - start_time
    return stop_time
