#!/usr/bin/env python3
"""
function named index_range
that takes two integer arguments
"""


def index_range(page, page_size):
    """return a tuple of size two
    containing a start index and an end index"""
    end = page_size * page
    start = (page - 1) * page_size
    return (start, end)
