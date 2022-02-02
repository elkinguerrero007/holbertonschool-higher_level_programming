#!/usr/bin/python3
"""
8-class_to_json.py
function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
"""


def class_to_json(obj):
    """return a dictionary"""
    return obj.__dict__
