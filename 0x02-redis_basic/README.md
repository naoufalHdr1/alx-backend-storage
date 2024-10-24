# 0x02. Redis Basic

## Description

This project involves learning how to use Redis for basic operations and implementing it as a simple caching system in Python. Redis is an open-source, in-memory data structure store used as a database, cache, and message broker. Through this project, we will explore key Redis commands and integrate Redis with Python.

## Learning Objectives

- Understand how to use Redis for basic operations.
- Learn to use Redis as a simple cache system.
- Familiarize with Redis commands like INCR, RPUSH, LPUSH, and more.
- Implement decorators in Python to count function calls and track the history of inputs and outputs using Redis.
- Build a web caching system using Redis.

## Setup Instructions

### Installing Redis on Ubuntu 18.04
```bash
$ sudo apt-get update
$ sudo apt-get install redis-server
```
### Python Redis Client Installation
```bash
$ pip3 install redis
```

### Starting Redis Server in a Container
```bash
$ sudo service redis-server start
```

## Tasks

### Task 0: Writing Strings to Redis

- Create a `Cache` class with a `store` method to store data in Redis with a random key.
- Use `uuid` to generate unique keys.
- Type-annotate to accept different data types: `str`, `bytes`, `int`, or `float`.

### Task 1: Reading from Redis and Recovering Original Type

- Implement a `get` method that retrieves data and uses an optional `Callable` to convert it to the original format.
- Add `get_str` and `get_int` methods to automatically convert Redis data to string and integer, respectively.

### Task 2: Incrementing Values

- Define a `count_calls` decorator to track how many times a method has been called.
- Store the count in Redis using the method's `__qualname__`.
- Decorate the `store` method with this decorator.

### Task 3: Storing Lists

- Implement a `call_history` decorator to log the input and output of a method.
- Store the history of inputs and outputs in separate Redis lists using `rpush`.
- Decorate the `store` method with this decorator.

### Task 4: Retrieving Lists

- Implement a `replay` function to display the call history of a function.
- Retrieve inputs and outputs from Redis and display them in the format `Cache.method(*args) -> output`.

### Task 5: Implementing an Expiring Web Cache and Tracker (Advanced)

- Implement a `get_page` function that caches the HTML content of a URL with an expiration time of 10 seconds.
- Track how many times a URL is accessed using Redis.
- Use `http://slowwly.robertomurray.co.uk` to simulate slow responses and test caching.
