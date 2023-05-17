#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data.update({key: item})

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
