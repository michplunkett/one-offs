"""Contains PDF-oriented utility functions."""

import os
from tempfile import TemporaryDirectory

from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string

from util.constants import (
    EXTENSION_JPEG,
    EXTENSION_PDF,
    FILE_TYPES_JPEG,
    STANDARD_DPI,
)


def get_files(input_folder: str):
    """Get file names from the specified directory."""
    file_names = []
    for f in os.listdir(input_folder):
        _, ext = os.path.splitext(f)
        if ext.lower() == EXTENSION_PDF.lower():
            file_names.append(f)

    return file_names


def get_file_text(file_name: str, input_folder: str):
    """Get the text stored in the specified file."""
    file_text = []
    image_file_list = []

    # Source: https://www.geeksforgeeks.org/python-reading-contents-of-pdf
    # -using-ocr-optical-character-recognition/
    with TemporaryDirectory() as tempdir:
        pdf_pages = convert_from_path(input_folder + file_name, STANDARD_DPI)

        for page_enumeration, page in enumerate(pdf_pages, start=1):
            # Create a file name to store the image
            filename = f"{tempdir}\\page_{page_enumeration:03}{EXTENSION_JPEG}"
            page.save(filename, FILE_TYPES_JPEG.upper())
            image_file_list.append(filename)

        for i, image_file in enumerate(image_file_list):
            text = str((image_to_string(Image.open(image_file))))
            file_text.append((i + 1, text))

    return file_text
