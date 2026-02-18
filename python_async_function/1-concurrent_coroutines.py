#!/usr/bin/env python3
"""
This module contains an asynchronous routine called wait_n that
spawns wait_random n times with the specified max_delay.
"""
import asyncio
from typing import List

# Import the previous function
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.

    Args:
        n (int): The number of times to spawn wait_random.
        max_delay (int): The maximum delay for each wait_random.

    Returns:
        List[float]: The list of all the delays (float values) in
        ascending order.
    """
    delays = []
    # Create a list of coroutine calls
    tasks = [wait_random(max_delay) for _ in range(n)]

    # as_completed yields tasks as they finish, regardless of start order
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
