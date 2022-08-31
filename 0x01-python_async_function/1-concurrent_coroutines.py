#!/usr/bin/env python3
"""execute multiple coroutines at the same time with async"""


from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """waits for a random delay between 0 and max_delay"""
    execs = []
    complete = []

    for i in range(n):
        exec = asyncio.create_task(wait_random(max_delay))
        execs.append(exec)

    for exec in asyncio.as_completed(execs):
        result: float = await exec
        complete.append(result)

    return complete
