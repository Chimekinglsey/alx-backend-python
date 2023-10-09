#!/usr/bin/env python3
"""
2.  Measure the runtime
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """returns mean execution time for wait_n"""
    start_exec = time.perf_counter()
    await wait_n(n, max_delay)
    stop_exec = time.perf_counter() - start_exec
    return  await stop_exec/n
