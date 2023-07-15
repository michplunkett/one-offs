"""File accessing and writing functions for the Google Translate API inputs and outputs."""

import csv
import os

from util.constants import (
    ENCODING_STANDARD,
    EXTENSION_CSV,
    FILE_OPEN_MODE_WRITE,
)

BASE_DIR = os.getcwd()
FOLDER_OUTPUT = BASE_DIR + "/google_translate_pdfs/data/output/"


def write_translation_to_csv(original_file_name, orig_text, trans_text):
    """Write translations to a .csv file."""
    name, _ = os.path.splitext(original_file_name)
    with open(
        FOLDER_OUTPUT + name + EXTENSION_CSV,
        FILE_OPEN_MODE_WRITE,
        encoding=ENCODING_STANDARD,
    ) as csv_file:
        writer = csv.writer(csv_file, delimiter="\t", quotechar='"')
        writer.writerow(["page", "original_text", "translated_text"])
        for i, text_tuple in enumerate(orig_text):
            writer.writerow(
                [
                    text_tuple[0],
                    text_tuple[1].replace("\t+", " ").replace("\n", " "),
                    trans_text[i],
                ]
            )
