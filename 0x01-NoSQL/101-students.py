#!/usr/bin/env python3
"""
This module provides a function to retrieve all students sorted by
their average score
"""


def top_students(mongo_collection):
    """
    Retrieves all students and calculates their average score.

    Args:
        mongo_collection : The MongoDB collection containing students' data.

    Returns:
        list: A list of students.
    """
    pipeline = [
        {
            '$addFields': {
                'averageScore': {
                    '$avg': '$topics.score'
                }
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
