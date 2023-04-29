"""
This file is a general file utility.
"""
import csv


def read_csv_to_dict(file_path):
    """
    This function reads in a CSV file path and then returns a dictionary of its
    respective keys and values.

    :param str file_path: This is the file path of the CSV file.
    :return: A key and value store of the CSV.
    :rtype Dictionary
    """
    return csv.DictReader(file_path)
