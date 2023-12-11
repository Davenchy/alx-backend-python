#!/usr/bin/env python3
"""generates a random value between 0 and max_delay and uses it as a delay"""
from asyncio import sleep
from random import random


async def wait_random(max_delay: int = 10) -> float:
    """generates a random value between 0 and max_delay and uses it as a delay
    after delay returns the value"""
    delay = random() * max_delay
    await sleep(delay)
    return delay
