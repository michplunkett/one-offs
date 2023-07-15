"""General file utility functions."""
import csv
import json

from util.constants import (
    ENCODING_STANDARD,
    FILE_OPEN_MODE_READ,
    FILE_OPEN_MODE_WRITE,
)


def read_csv_to_dict(file_path):
    """Read in a CSV file path and then return a dictionary of its respective keys and values."""
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
    """Write a dictionary to a JSON file."""
    with open(
        file_path, encoding=ENCODING_STANDARD, mode=FILE_OPEN_MODE_WRITE
    ) as out_file:
        json.dump(json_dict, out_file, indent=4)
