#!/usr/bin/env python3
"""
This module contains the `insert_school` function that allows inserting
a new document with provided keyword arguments.
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in the MongoDB collection.

    Args:
    mongo_collection : The pymongo collection object.
    **kwargs: Arbitrary keyword arguments that represent the fields of
    the new document.

    Returns:
    bson.ObjectId: The _id of the inserted document.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
