#!/usr/bin/env python3
"""Ceci est une description"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """Ceci est une description"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
