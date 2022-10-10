#!/usr/bin/env python3
"""This file is to test the basic functions and methods in association
with redis"""


import redis
import uuid
from typing import Callable


class Cache():
    """Class for Redis client instance"""

    def __init__(self) -> None:
        """Instantiates class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """Takes data argument and generates a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> str | int:
        """Reading from Redis and recovering original type"""
        if key:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Automatically parameterize"""
        return self.get(key, str)


    def get_int(self, key: str) -> int:
        """Automatically parameterize"""
        return self.get(key, int)
