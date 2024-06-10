#!/usr/bin/env python3

'''
Module to create a task that calls the task_wait_random coroutine.
'''

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''
    Asynchronously spawns task_wait_random n times with the specified delay.

    Args:
        n (int): The number of times to spawn task_wait_random.
        max_delay (int): The maximum delay in seconds.

    Returns:
        List[float]: A list of delays in ascending order.
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))
