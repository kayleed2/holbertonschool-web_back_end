#!/usr/bin/env python3
"""Python function that changes all topics of a school document based on the name"""


def update_topics(mongo_collection, name, topics):
    """changes all topics of a school document"""
    if mongo_collection:
        mongo_collection.update(
            {name: name},
            { $set: {topics: topics}},
            {
                multi: true
            }
        )
    else:
        return []
