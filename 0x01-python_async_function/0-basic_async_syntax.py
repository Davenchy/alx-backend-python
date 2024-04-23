#!/usr/bin/env python3
"""generates a random value between 0 and max_delay and uses it as a delay"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """generates a random value between 0 and max_delay and uses it as a delay
    after delay returns the value"""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
