#!/usr/bin/env python3
"""Ceci est une description"""
from typing import Tuple


def index_range(page, page_size):
    """Ceci est une description"""
    start = (page - 1) * page_size
    end = page + page_size
    return start, end
