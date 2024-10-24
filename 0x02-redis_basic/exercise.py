#!/usr/bin/env python3
"""
This module defines a Cache class that interacts with a Redis database
for caching arbitrary data types. The data is stored using a randomly
generated key, and the key is returned to the caller.
"""
import redis
import uuid
from typing import Union


class Cache:
    """
    Cache class that uses Redis as the backend to store data.
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in Redis using a randomly generated key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)

        return key
