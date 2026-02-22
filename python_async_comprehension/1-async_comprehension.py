#!/usr/bin/env python3
"""documented"""
from typing import List
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """it collects random numbers and lists them"""
    return [i async for i in async_generator()]
