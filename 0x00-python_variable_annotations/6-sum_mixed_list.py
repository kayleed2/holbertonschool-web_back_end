#!/usr/bin/env python3


from typing import Union, List


thing = Union[int, float]


def sum_mixed_list(mxd_lst: List[thing]) -> float:
    return sum(mxd_lst)
