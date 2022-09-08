#!/usr/bin/env python3
"""
module for simple pagination
"""


import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initiates server class"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Function to get page"""
        try:
            assert type(page) == int and type(page_size) == int
            assert page > 0 and page_size > 0
            r = index_range(page, page_size)
            list_of_rows = []
            with open(self.DATA_FILE, mode='r') as csv_file:
                csv_reader = csv.reader(csv_file)
                line_count = 0
                for row in csv_reader:
                    if line_count == 0:
                        line_count += 1
                        continue
                    if line_count > r[0] and line_count <= r[1]:
                        list_of_rows.append(row)
                    line_count += 1
            return list_of_rows

        except AssertionError:
            raise AssertionError


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
