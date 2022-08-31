#!/usr/bin/env python3


from typing import Union, Tuple


thing = Union[int, float]


def to_kv(k: str, v: thing) -> Tuple[str, float]:
    return k, v**2
