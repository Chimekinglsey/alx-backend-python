#!/usr/bin/env python3
"""
 102. Type Checking
"""
from typing import Tuple, List, Any, Mapping


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """zooms and array based on provided zoom value"""
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
