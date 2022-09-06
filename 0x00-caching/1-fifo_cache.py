#!/usr/bin/python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system:
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ 
    class FIFOCache that
    inherits from BaseCaching and
    is a caching system:
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key and item):
            self.cache_data[key] = item
        dict_list = list(self.cache_data)
        if ((len(self.cache_data) > super().MAX_ITEMS)):
            del self.cache_data[dict_list[0]]
            print("DISCARD:", dict_list[0])

    def get(self, key):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
