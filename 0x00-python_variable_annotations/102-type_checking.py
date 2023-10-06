#!/usr/bin/env python3
"""
102. Type Checking
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List[Any]:
    """zooms an array based on the provided zoom factor"""
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
