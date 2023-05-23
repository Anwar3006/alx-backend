#!/usr/bin/env python3
"""
LRU Caching
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Implementing the LRU caching replacement policy
    if cache size is reached; the least recent entry is replaced
    with incoming entry
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None and item is None:
            return

        self.cache_data[key] = item
            # move lru_key to after the current key
                # print(f"found key {key} ---- element {element}")
                # print(keyList)
                # print(keyList[index + 1])
        #         print(track_key)
        # if key in keyList:
        #     print(f"this is {key}")
        # print(keyList)
        keyList = list(self.cache_data.keys())
        track_key = "0"
        for index, element in enumerate(keyList):
            if element == key:
                # track_key = keyList[index + 1]
                print(keyList)
            # if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            #     del_key = self.cache_data.pop(track_key)
            #     print(f"DISCARD: {del_key}")

        try:
            # remove item based on the incoming key if key is in self.cache_data
            self.cache_data.pop(key)
        except KeyError:
            # else key not in dict; remove first item
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if track_key in self.cache_data.keys():
                    del_key = self.cache_data.pop(track_key)
                else:
                    del_key, _ = self.cache_data.popitem(last=False)
                print(f"DISCARD: {del_key}")
        # if key in self.cache_data:
        # self.cache_data[key] = item
        
        # if len(self.cache_data) > BaseCaching.MAX_ITEMS:
        #     cache_list = iter(self.cache_data)
        #     oldest = next(cache_list)
        #     print(oldest)

        #     # for k in cache_list:
        #         # if k == key and k in self.cache_data
        #     # print(after_oldest)
        #     # del self.cache_data[oldest]

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
