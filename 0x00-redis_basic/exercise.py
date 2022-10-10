#!/usr/bin/env python3
"""This file is to test the basic functions and methods in association
with redis"""


import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Counts calls to a method"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        """Function to increment the count for specific method"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Function to add input parameters to Redis list"""

    @wraps(method)
    def wrapper(self, *args) -> Union[int, str]:
        """Stores call history into lists"""
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args)
        self._redis.rpush(f"{key}:outputs", output)
        return output

    return wrapper


def replay(method: Callable) -> None:
    """Gets the method call history from redis db"""
    lr = redis.Redis()
    name = method.__qualname__

    inputs = lr.lrange(f"{name}:inputs", 0, -1)
    outputs = lr.lrange(f"{name}:outputs", 0, -1)
    print(f"{name} was called {len(inputs)} times:")

    for i, o in zip(inputs, outputs):
        print(f"{name}(*{(i).decode('utf-8')}) -> {(o).decode('utf-8')}")


class Cache():
    """Class for Redis client instance"""

    def __init__(self) -> None:
        """Instantiates class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Takes data argument and generates a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, int]:
        """Reading from Redis and recovering original type"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Automatically parameterize"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Automatically parameterize"""
        return self.get(key, int)
