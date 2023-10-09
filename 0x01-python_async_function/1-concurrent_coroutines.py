#!/usr/bin/env python3
"""
1. Execute  multiple coroutines at the same time with async
"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """Spawn wait_random n times with the specified max_delay and return the delays in ascending order."""
    delays = []  # List to store the delays
    
    async def collect_delay(task):
        delay = await task
        # Insert delay into the sorted position in the delays list
        for i in range(len(delays)):
            if delay < delays[i]:
                delays.insert(i, delay)
                break
        else:
            delays.append(delay)
    
    tasks = [wait_random(max_delay) for _ in range(n)]
    await asyncio.gather(*(collect_delay(task) for task in tasks))
    
    return delays
# async def wait_n(n: int, max_delay: int) -> List[float]:
#     """returns a list of random floats """
#     wait_list: List[float] = []
#     for i in range(n):
#         result = await wait_random(max_delay)
#         wait_list.append(result)

#     for item in range(len(wait_list)):
#         for i in range(len(wait_list) - item - 1):
#             if wait_list[i] > wait_list[i + 1]:
#                 wait_list[i], wait_list[i + 1] = wait_list[i + 1], wait_list[i]
      
#     return wait_list
