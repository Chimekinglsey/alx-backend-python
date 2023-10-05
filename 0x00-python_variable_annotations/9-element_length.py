#!/usr/bin/env python3
"""
 9. Let's duck type an iterable object
"""
from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns duck or annotation for subscriptibles"""
    return [(i, len(i)) for i in lst]
