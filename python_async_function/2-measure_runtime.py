#!/usr/bin/env python3
"""function for python """
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 4, max_delay: int = 5) -> float:
    """measuring time"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    result = (end_time - start_time) / n

    return result