#!/usr/bin/env python3
"""
This module defines a Cache class that interacts with a Redis database
for caching arbitrary data types. The data is stored using a randomly
generated key, and the key is returned to the caller.
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def call_history(method: Callable) -> Callable:
    """
    Decorator to store the history of inputs and outputs for a function
    in Redis.
    Inputs are stored in a list with the key `method.__qualname__:inputs`.
    Outputs are stored in a list with the key `method.__qualname__:outputs`.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function that logs inputs and outputs in Redis."""
        # Create Redis keys for inputs and outputs
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Log the inputs by appending them to the inputs list
        self._redis.rpush(input_key, str(args))

        # Execute the original method
        output = method(self, *args, **kwargs)

        # Log the output by appending it to the outputs list
        self._redis.rpush(output_key, str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """
    Decorator to count how many times a method is called.
    The count is stored in Redis using the method's qualified name.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Wrapper function that increments the call count in Redis."""
        # Increment the call count using Redis INCR command
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)

        # Call the original method
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """
    Cache class that uses Redis as the backend to store data.
    """

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
        if data is None:
            return None

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

    def replay(self, method: Callable):
        """Display the history of calls for a given method."""
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        inputs = self._redis.lrange(input_key, 0, -1)
        outputs = self._redis.lrange(output_key, 0, -1)

        # Print the replay output
        print(f"{method.__qualname__} was called {len(inputs)} times:")
        for input_val, output_val in zip(inputs, outputs):
            print(
                    f"{method.__qualname__}(*{input_val.decode('utf-8')}) "
                    f"-> {output_val.decode('utf-8')}"
            )
