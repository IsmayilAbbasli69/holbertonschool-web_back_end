#!/usr/bin/env python3
"""pagination"""
import csv
from typing import List


def index_range(page=1, page_size=10):
    """using pagination"""
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """baby names"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """INit file, if you dunno"""
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
        """function"""
        data = self.dataset()
        assert isinstance(page, int) and page > 0, "Cant be the 0"
        assert isinstance(page, int) and page_size > 0, "Cant be the 0!"
        try:
            start, end = index_range(page, page_size)
            return data[start:end]
        except IndexError:
            return []
