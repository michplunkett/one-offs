"""
This file houses the file accessing and writing functions for the Google
Translate API inputs and outputs.
"""

import csv
import os
import pdfplumber
from util.constants import ENCODING_STANDARD

BASE_DIR = os.getcwd()
FOLDER_INPUT = BASE_DIR + "/google_translate_pdfs/data/input/"
FOLDER_OUTPUT = BASE_DIR + "/google_translate_pdfs/data/output/"


def get_files_to_translate(extension=""):
    file_names = []
    for f in os.listdir(FOLDER_INPUT):
        _, ext = os.path.splitext(f)
        if (
            extension != "" and ext.lower() == extension.lower()
        ) or extension == "":
            file_names.append(f.replace("\t+", " ").replace("\n", " "))

    return file_names


def get_file_text(file_name):
    file_text = []
    with pdfplumber.open(FOLDER_INPUT + file_name) as pdf:
        for page in pdf.pages:
            file_text.append(
                page.extract_text(
                    x_tolerance=3,
                    y_tolerance=3,
                    layout=False,
                    x_density=7.25,
                    y_density=13,
                )
                .replace("\t+", " ")
                .replace("\n", " ")
            )

    return file_text


def write_translation_to_csv(original_file_name, orig_text, trans_text):
    name, _ = os.path.splitext(original_file_name)
    with open(
        FOLDER_OUTPUT + name + ".csv",
        "w",
        encoding=ENCODING_STANDARD,
    ) as csv_file:
        writer = csv.writer(csv_file, delimiter="\t", quotechar='"')
        writer.writerow(["page", "original_text", "translated_text"])
        for i, text in enumerate(orig_text):
            writer.writerow([i + 1, text, trans_text[i]])
