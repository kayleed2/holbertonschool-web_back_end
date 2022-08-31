#!/usr/bin/env python3
"""Learning typing annotations for python 3.7++"""


from typing import Union, List


thing = Union[int, float]


def sum_mixed_list(mxd_lst: List[thing]) -> float:
    """Function to get sum of mixed int float list"""
    return sum(mxd_lst)
