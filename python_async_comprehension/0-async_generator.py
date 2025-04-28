#!/usr/bin/env python3
"""Ceci est une description"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Ceci est une description"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)