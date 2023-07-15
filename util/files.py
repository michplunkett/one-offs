"""This file is a general file utility."""
import csv
import json

from util.constants import (
    ENCODING_STANDARD,
    FILE_OPEN_MODE_READ,
    FILE_OPEN_MODE_WRITE,
)


def read_csv_to_dict(file_path):
    """
    This function reads in a CSV file path and then returns a dictionary of its
    respective keys and values.

    :param str file_path: This is the file path of the CSV file.
    :return: A key and value store of the CSV.
    :rtype Dictionary
    """
    rows = []

    with open(
        file_path,
        encoding=ENCODING_STANDARD,
        mode=FILE_OPEN_MODE_READ,
        newline="",
    ) as csv_file:
        reader = csv.DictReader(csv_file)
        for r in reader:
            rows.append(r)

    return rows


def write_to_json(file_path, json_dict):
    """
    This function writes a dictionary to a JSON file.

    :param str file_path: The path of the desired file.
    :param dict json_dict: A dictionary meant to be written as JSON.
    """
    with open(
        file_path, encoding=ENCODING_STANDARD, mode=FILE_OPEN_MODE_WRITE
    ) as out_file:
        json.dump(json_dict, out_file, indent=4)
