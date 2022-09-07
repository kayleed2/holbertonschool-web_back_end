#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    class LIFOCache that
    inherits from BaseCaching and
    is a caching system:
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        self.cache_data = OrderedDict(self.cache_data)
        if (key and item):
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.popitem(last = False)
                print("DISCARD:", key)

    def get(self, key):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
