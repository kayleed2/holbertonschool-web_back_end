#!/usr/bin/env python3
"""Python function that inserts a new document in a collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """ inserts a new document in a collection"""
    for k, v in kwargs:
        mongo_collection.insert({k:v})
    return mongo_collection.find({k:v}).id
