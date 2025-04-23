#!/usr/bin/env python3
"""Ceci est une description"""
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Ceci est une description"""
    return [(i, len(i)) for i in lst]
