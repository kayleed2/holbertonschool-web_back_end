#!/usr/bin/env python3
"""
function named index_range
that takes two integer arguments
"""


from turtle import st


def index_range(page, page_size):
    """return a tuple of size two
    containing a start index and an end index"""
    if page == 0 and page_size:
        end = page_size
        start = 0
        return (start, end)
    
    if (page and page_size):
        end = page_size * page
        start = (page - 1) * page_size
        return (start, end)
