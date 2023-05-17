#!/usr/bin/env python3
"""
FIFO Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """
    Implementing the FIFO caching replacement policy
    if cache size is reached; the first entry is replaced
    with incoming entry
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key, first_item = self.cache_data.popitem(last=False)
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
