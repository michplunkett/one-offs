"""
This file is a general file utility.
"""
import csv

from util.constants import ENCODING_STANDARD


def read_csv_to_dict(file_path):
    """
    This function reads in a CSV file path and then returns a dictionary of its
    respective keys and values.

    :param str file_path: This is the file path of the CSV file.
    :return: A key and value store of the CSV.
    :rtype Dictionary
    """
    rows = []

    with open(file_path, newline="", encoding=ENCODING_STANDARD) as csvfile:
        reader = csv.DictReader(csvfile)
        for r in reader:
            rows.append(r)

    return rows
