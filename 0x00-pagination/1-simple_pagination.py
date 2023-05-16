#!/usr/bin/env python3
"""
Simple pagination
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    returns a tuple of a page and the search hits that will be on the page
    """
    return_page = []
    if page and page_size:
        if page == 1:
            return_page.append(page - 1)
            return_page.append(page_size)
        else:
            startIndex = page_size * (page - 1)
            endIndex = page_size * (page)
            return_page.append(startIndex)
            return_page.append(endIndex)
    return tuple(return_page)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
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
        """
        get pages based on pagination range
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        page1 = list(index_range(page, page_size))
        dataset = self.dataset()

        new_list = []
        for data in dataset[page1[0]: page1[1]]:
            new_list.append(data)
        return new_list
