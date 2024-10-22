#!/usr/bin/env python3
"""
Module to list all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.

    Args:
    mongo_collection : The pymongo collection object.

    Returns:
    list: A list of all documents in the collection.
    """
    return mongo_collection.find()
