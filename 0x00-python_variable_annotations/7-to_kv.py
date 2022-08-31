#!/usr/bin/env python3
"""Learning typing annotations for python 3.7++"""


from typing import Union, Tuple


thing = Union[int, float]


def to_kv(k: str, v: thing) -> Tuple[str, float]:
    """Function to get the squared version of a variable"""
    return k, v**2
