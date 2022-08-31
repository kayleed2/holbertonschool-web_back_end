#!/usr/bin/env python3

import typing
thing = typing.List[typing.Tuple[typing.Sequence, int]]


def element_length(lst: typing.Iterable[typing.Sequence]) -> thing:
    return [(i, len(i)) for i in lst]
