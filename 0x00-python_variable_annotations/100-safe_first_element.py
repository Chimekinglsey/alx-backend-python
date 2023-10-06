#!/usr/bin/env python3
"""
 100. duck type an iterable object
"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """annotate unknown input type"""
    if lst:
        return lst[0]
    else:
        return None
