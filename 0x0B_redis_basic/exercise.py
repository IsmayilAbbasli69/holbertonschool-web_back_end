#!/usr/bin/env python3
"""This module contains the Cache class"""
import redis
import uuid
from typing import Union, Callable
from functools import wraps


def call_history(method: Callable) -> Callable:
    """Decorator to store the history"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function."""
        key = method.__qualname__
        self._redis.rpush(f"{key}:inputs", str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(f"{key}:outputs", str(output))
        return output
    return wrapper


def count_calls(method: Callable) -> Callable:
    """Counts the number of times"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function."""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


class Cache():
    """Cache class."""

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Generates a random key"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable[[bytes], str] = None) -> str:
        """Retrieves the value associated with the key from Redis"""
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> str:
        """Automatically parameterizes <Cache.get> with the correct"""
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """Automatically parameterizes <Cache.get> with the correct"""
        return self.get(key, int)


def replay(method: Callable) -> Callable:
    """Displays the history of calls of a particular function."""
    instance = redis.Redis()
    qn = method.__qualname__
    inputs = instance.lrange(f"{qn}:inputs", 0, -1)
    outputs = instance.lrange(f"{qn}:outputs", 0, -1)
    print("{} was called {} times:".format(qn, len(inputs)))
    for input, output in zip(inputs, outputs):
        print(f"{qn}(*{input.decode('UTF-8')}) -> {output}")
