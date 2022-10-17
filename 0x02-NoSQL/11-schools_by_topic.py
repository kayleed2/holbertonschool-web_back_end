#!/usr/bin/env python3
"""Python function that returns the list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    if mongo_collection:
        mongo_collection.find({'topics': topic})
    else:
        return []
