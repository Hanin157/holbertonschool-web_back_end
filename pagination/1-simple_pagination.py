#!/usr/bin/env python3
"""
Module that implements simple pagination for a dataset.
"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return start and end indexes for pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the server with no cached dataset.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Return the cached dataset from the CSV file.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return one page of the dataset using page and page size.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)

        return self.dataset()[start_index:end_index]
