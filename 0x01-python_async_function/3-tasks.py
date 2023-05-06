#!/usr/bin/env python3
""" task_wait_random function """

from asyncio import Task, create_task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """ random task wait """
    ret = create_task(wait_random(max_delay))
    return ret
