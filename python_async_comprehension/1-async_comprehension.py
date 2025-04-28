#!/usr/bin/env python3
"""Ceci est une description"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Ceci est une description"""
    result = []
    async for i in async_generator():
        result.append(i)
    return result
