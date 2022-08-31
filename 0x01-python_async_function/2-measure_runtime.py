#!/usr/bin/env python3
'''
Create a measure_time function with integers n
and max_delay as arguments that measures the total
execution time for wait_n(n, max_delay), and returns total_time / n
'''


import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """Using time module to measure time execution of function / process"""
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish = time.time()
    return (finish - start) / n
