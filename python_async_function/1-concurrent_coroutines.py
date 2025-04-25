#!/usr/bin/env python3
"""Ceci est une description"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Ceci est une description"""
    delays = []
    for task in asyncio.as_completed([wait_random(max_delay) for _ in range(n)]):
        delay = await task
        delays.append(delay)
    return delays
