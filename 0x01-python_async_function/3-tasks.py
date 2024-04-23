#!/usr/bin/env python3
"""This module contains task_wait_random function"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """returns the wait_random coroutine as a task"""
    return asyncio.create_task(wait_random(max_delay))
