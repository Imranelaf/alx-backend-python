#!/usr/bin/env python3

'''
Module to measure the runtime of the wait_n coroutine
'''

import asyncio
import time

wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
    Measure the total execution time for wait_n(n, max_delay) and returns
    the average time per task.

    Args:
        n (int): Number of tasks to run.
        max_delay (int): Maximum delay for each task.

    Returns:
        float: Average time per task.
    '''
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()

    return (end_time - start_time) / n
