#!/usr/bin/env python3
"""
This module defines a Cache class that interacts with a Redis database
for caching arbitrary data types. The data is stored using a randomly
generated key, and the key is returned to the caller.
"""
import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(
            self,
            key: str,
            fn: Optional[Callable] = None
            ) -> Union[str, bytes, int, float, None]:
        """
        Retrieve the data from Redis by key and optionally apply
        a transformation.
        """
        data = self._redis.get(key)

        return fn(data) if fn is not None else data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve a string from Redis by key.
        """
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve an integer from Redis by key.
        """
        return self.get(key, lambda d: int(d))
