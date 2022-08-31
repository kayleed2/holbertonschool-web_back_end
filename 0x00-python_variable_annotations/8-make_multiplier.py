#!/usr/bin/env python3
"""Learning typing annotations for python 3.7++"""


from typing import Callable
x = Callable[[float], float]


def make_multiplier(multiplier: float) -> x:
    """Function to create a multiplier function"""
    def inner_func(val: float) -> float:
        """Inner function to get the resulting value"""
        return (val * multiplier)
    return inner_func
