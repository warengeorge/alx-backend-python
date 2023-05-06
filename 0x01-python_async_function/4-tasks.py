#!/usr/bin/env python3
""" task_wait_n function """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    "task with for n number"
    asy_task = [task_wait_random(max_delay) for _ in range(n)]
    return [await ts for ts in asyncio.as_completed(asy_task)]
