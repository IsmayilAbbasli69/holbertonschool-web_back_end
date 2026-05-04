#!/usr/bin/env python3
"""pagination"""

import csv
from typing import List, Dict, Union


class Server:
    """Server baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """datasets"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    b = Dict[int, object]

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> b:
        """
        We use this method for give some information about this stuff
        """
        assert index is not None and index >= 0
        assert isinstance(page_size, int) and page_size > 0

        all_data = self.indexed_dataset()
        assert index < len(all_data)

        data = []
        current_idx = index

        while len(data) < page_size and current_idx < len(all_data):
            item = all_data.get(current_idx)
            if item:
                data.append(item)
            current_idx += 1

        next_index = current_idx if current_idx < len(all_data) else None

        return {'index': index,
                'data': data,
                'page_size': len(data),
                'next_index': next_index}
