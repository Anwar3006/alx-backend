#!/usr/bin/env python3
"""
LIFO Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """
    Implementing the LIFO caching replacement policy
    if cache size is reached; the last entry is replaced
    with incoming entry
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            return self.cache_data.update({key: item})

        if len(self.cache_data) == BaseCaching.MAX_ITEMS:
            last_key, last_item = self.cache_data.popitem(last=True)
            print(f"DISCARD: {last_key}")
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key)
