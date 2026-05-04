#!/usr/bin/env python3
import asyncio
import time
from asyncio import gather
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end_time = time.perf_counter()
    final_time = end_time - start_time
    return final_time

if __name__ == "__main__":
    total_runtime = asyncio.run(measure_runtime())
    print(f"Total runtime: {total_runtime:.2f} seconds")
