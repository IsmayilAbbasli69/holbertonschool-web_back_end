#!/usr/bin/env python3
"""0-async_generator.py"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """funct that generates random float number for 10 times every second
"""
    for i in range(10):
        await asyncio.sleep(1)
        number: float = random.uniform(0, 10)
        yield number
