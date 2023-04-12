"""
This file houses the file accessing and writing functions for the Google
Translate API inputs and outputs.
"""

import csv
import os
from tempfile import TemporaryDirectory

from pytesseract import image_to_string
from pdf2image import convert_from_path
from PIL import Image

from util.constants import (
    ENCODING_STANDARD,
    EXTENSION_CSV,
    EXTENSION_JPEG,
    EXTENSION_PDF,
    FILE_OPEN_WRITE,
    FILE_TYPES_JPEG,
    STANDARD_DPI,
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
    file_text = []
    image_file_list = []

    # Source: https://www.geeksforgeeks.org/python-reading-contents-of-pdf
    # -using-ocr-optical-character-recognition/
    with TemporaryDirectory() as tempdir:
        pdf_pages = convert_from_path(FOLDER_INPUT + file_name, STANDARD_DPI)

        for page_enumeration, page in enumerate(pdf_pages, start=1):
            # Create a file name to store the image
            filename = f"{tempdir}\\page_{page_enumeration:03}{EXTENSION_JPEG}"
            page.save(filename, FILE_TYPES_JPEG.upper())
            image_file_list.append(filename)

        for i, image_file in enumerate(image_file_list):
            text = str((image_to_string(Image.open(image_file))))
            file_text.append(
                (
                    i + 1,
                    text.replace("\t+", " ").replace("\n", " "),
                )
            )

    return file_text


def write_translation_to_csv(original_file_name, orig_text, trans_text):
    name, _ = os.path.splitext(original_file_name)
    with open(
        FOLDER_OUTPUT + name + EXTENSION_CSV,
        FILE_OPEN_WRITE,
        encoding=ENCODING_STANDARD,
    ) as csv_file:
        writer = csv.writer(csv_file, delimiter="\t", quotechar='"')
        writer.writerow(["page", "original_text", "translated_text"])
        for i, text_tuple in enumerate(orig_text):
            writer.writerow([text_tuple[0], text_tuple[1], trans_text[i]])
