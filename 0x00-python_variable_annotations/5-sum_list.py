#!/usr/bin/env python3
"""Learning typing annotations for python 3.7++"""


import typing


thing = typing.List[float]


def sum_list(input_list: thing) -> float:
    """Function to get the sum of a list with type annotations"""
    return sum(input_list)
