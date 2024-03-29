#!/usr/bin/env python3
"""Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """Lists all documents in" collection"""
    if mongo_collection.find():
        return mongo_collection.find()
    else:
        return []
