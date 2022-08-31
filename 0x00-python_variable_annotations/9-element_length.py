#!/usr/bin/env python3
"""Learning typing annotations for python 3.7++"""


import typing
thing = typing.List[typing.Tuple[typing.Sequence, int]]


def element_length(lst: typing.Iterable[typing.Sequence]) -> thing:
    """Function to return length of element using for loop"""
    return [(i, len(i)) for i in lst]
