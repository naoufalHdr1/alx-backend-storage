#!/usr/bin/env python3
"""
Module to search schools by topic in a MongoDB collection.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
    mongo_collection: The pymongo collection object.
    topic (str): The topic to search for in the schools' topics.

    Returns:
    list: List of schools that have the specified topic.
    """
    return mongo_collection.find({"topics": topic})
