"""Contains functions for writing .pdf output."""
import os

from util.constants import (
    ENCODING_STANDARD,
    EXTENSION_TXT,
    FILE_OPEN_MODE_WRITE,
)


FOLDER_OUTPUT = os.getcwd() + "/pdf_parser/data/output/"


def write_file_text_to_txt(original_file_name, text):
    """Write file text to a .txt file."""
    name, _ = os.path.splitext(original_file_name)
    with open(
        FOLDER_OUTPUT + name + EXTENSION_TXT,
        FILE_OPEN_MODE_WRITE,
        encoding=ENCODING_STANDARD,
    ) as text_file:
        text_file.writelines(text)
