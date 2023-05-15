#!/usr/bin/env python3
"""
Simple helper function
"""


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
