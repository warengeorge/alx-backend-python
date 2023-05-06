#!/usr/bin/env python3
""" execute multiple coroutines async """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ async spawn random n values"""
    asy_task = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    ret = [await t for t in asyncio.as_completed(asy_task)]
    return ret
