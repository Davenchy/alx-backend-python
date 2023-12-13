#!/usr/bin/env python3
""" Run Async Comprehensions using asyncio and measure the runtime """
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """run async comprehensions using asyncio 4 times in parallel and measure
    the runtime then return it"""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elapsed = time.perf_counter() - start
    return elapsed
