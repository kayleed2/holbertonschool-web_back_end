#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that
    inherits from BaseCaching and
    is a caching system:
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if (key and item):
            if (key in self.cache_data):
                self.cache_data.pop(key)
            self.cache_data[key] = item

            if ((len(self.cache_data) > BaseCaching.MAX_ITEMS)):
                dict_list = list(self.cache_data)
                el = dict_list[BaseCaching.MAX_ITEMS - 1]
                del self.cache_data[el]
                print("DISCARD:", el[0])

    def get(self, key):
        """ Get an item by key
        """
        if (key is None or key not in self.cache_data):
            return None
        return self.cache_data[key]
