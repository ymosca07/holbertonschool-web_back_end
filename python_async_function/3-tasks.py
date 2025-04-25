#!/usr/bin/env python3
"""Ceci est une description"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Cecfi est une description"""
    return asyncio.create_task(wait_random(max_delay))
