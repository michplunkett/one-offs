"""
This file houses the file accessing and writing functions for the Google
Translate API inputs and outputs.
"""

import csv
import io
import os

from pdfminer.converter import TextConverter
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from util.constants import (
    ENCODING_STANDARD,
    EXTENSION_PDF,
    FILE_OPEN_MODE_BINARY_READ,
)

BASE_DIR = os.getcwd()
FOLDER_INPUT = BASE_DIR + "/google_translate_pdfs/data/input/"
FOLDER_OUTPUT = BASE_DIR + "/google_translate_pdfs/data/output/"


def get_files_to_translate():
    file_names = []
    for f in os.listdir(FOLDER_INPUT):
        _, ext = os.path.splitext(f)
        if ext.lower() == EXTENSION_PDF.lower():
            file_names.append(f)

    return file_names


def get_file_text(file_name):
    fp = open(FOLDER_INPUT + file_name, FILE_OPEN_MODE_BINARY_READ)
    resource_manager = PDFResourceManager()
    return_str = io.StringIO()
    device = TextConverter(
        resource_manager,
        return_str,
        codec=ENCODING_STANDARD,
        laparams=LAParams(),
    )
    interpreter = PDFPageInterpreter(resource_manager, device)
    file_text = []
    for pageNumber, page in enumerate(PDFPage.get_pages(fp)):
        interpreter.process_page(page)
        print(return_str.getvalue().encode(ENCODING_STANDARD))
        # file_text.append(
        #     return_str.getvalue()
        #     .encode(ENCODING_STANDARD)
        # )

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
