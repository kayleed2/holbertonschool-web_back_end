#!/usr/bin/env python3

from typing import Callable
x = Callable[[float], float]


def make_multiplier(multiplier: float) -> x:
    return x()
