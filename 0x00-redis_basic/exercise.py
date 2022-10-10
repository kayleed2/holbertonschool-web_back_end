#!/usr/bin/env python3
"""This file is to test the basic functions and methods in association
with redis"""


import redis
import uuid


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
