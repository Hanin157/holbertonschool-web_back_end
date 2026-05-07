#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

import csv
import math
from typing import Dict, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initialize the server with empty cached datasets.
        """
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Return the dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(
            self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a deletion-resilient page with hypermedia metadata.
        """
        dataset = self.indexed_dataset()
        assert index is not None and isinstance(index, int)
        assert index >= 0 and index < len(self.dataset())

        data = []
        next_index = index

        while len(data) < page_size and next_index < len(self.dataset()):
            if next_index in dataset:
                data.append(dataset[next_index])
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
