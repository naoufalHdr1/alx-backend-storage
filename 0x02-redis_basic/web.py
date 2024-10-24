import requests
import redis
from functools import wraps
from urllib.parse import quote

# Initialize the Redis client
redis_client = redis.Redis()


def cache_page(func):
    """Decorator to cache page content and track URL access."""
    @wraps(func)
    def wrapper(url: str) -> str:
        # Create cache key
        cache_key = f"page:{quote(url)}"
        count_key = f"count:{quote(url)}"

        # Check if the page content is already cached
        cached_content = redis_client.get(cache_key)
        if cached_content:
            # If cached, increment access count and return cached content
            redis_client.incr(count_key)
            return cached_content.decode('utf-8')

        # Fetch the content using the original function
        content = func(url)

        # Cache the content with an expiration time of 10 seconds
        redis_client.setex(cache_key, 10, content)

        # Increment the access count
        redis_client.incr(count_key)

        return content

    return wrapper


@cache_page
def get_page(url: str) -> str:
    """Fetch the HTML content of a URL."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.text
