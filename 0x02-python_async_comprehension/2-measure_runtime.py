#!/usr/bin/env python3
"""coroutine that will execute async_comprehension
four times in parallel using asyncio.gather"""


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension())
    end = time.time()
    return (end - start)
