#!/usr/bin/env python3
""" a coroutine that will execute async_comprehension four times in
    parallel using asyncio.gather """
import asyncio
import time
from importlib import import_module as using


async_comprehension = using('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """async_comprehension is excuted 4 times and measures the
    total execution time."""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    result = time.time() - start_time
    return result
