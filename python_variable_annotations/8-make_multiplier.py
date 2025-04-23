#!/usr/bin/env python3
"""Ceci est une description"""
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Ceci est une description"""
    return lambda x: x * multiplier
