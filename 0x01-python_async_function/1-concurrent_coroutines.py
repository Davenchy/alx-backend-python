#!/usr/bin/env python3
""""""
import asyncio
from typing import List

wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """returns the list of all the delays"""
    results = await asyncio.gather(
        *[asyncio.create_task(wait_random(max_delay)) for _ in range(n)],
    )
    return sorted(results)
