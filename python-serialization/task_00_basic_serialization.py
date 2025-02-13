#!/usr/bin/env python3
"""
Module for basic JSON serialization and deserialization.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The Python dictionary to serialize
        filename (str): The name of the output JSON file

    Returns:
        None
    """
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file)
    except Exception as e:
        print(f"Error serializing data: {str(e)}")


def load_and_deserialize(filename):
    """
    Load and deserialize data from a JSON file.

    Args:
        filename (str): The name of the input JSON file

    Returns:
        dict: The deserialized Python dictionary
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error deserializing data: {str(e)}")
        return None
