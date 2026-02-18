#!/usr/bin/env python3
"""
This is basic async function
"""
import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    Here I add function here
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
