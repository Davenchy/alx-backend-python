#!/usr/bin/env python3
"""This module has an AsyncGenerator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """This AsyncGenerator returns 10 random floats between 0 and 10 every
    second"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
