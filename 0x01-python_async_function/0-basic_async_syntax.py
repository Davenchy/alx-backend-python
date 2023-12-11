#!/usr/bin/env python3
"""generates a random value between 0 and max_delay and uses it as a delay"""
from asyncio import sleep
from random import uniform


async def wait_random(max_delay: float = 10) -> float:
    """generates a random value between 0 and max_delay and uses it as a delay
    after delay returns the value"""
    delay = uniform(0, max_delay)
    await sleep(delay)
    return delay
