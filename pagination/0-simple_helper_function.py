#!/usr/bin/env python3
"""Ceci est une description"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Ceci est une description"""
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
