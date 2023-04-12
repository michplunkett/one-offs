import os

from util.constants import (
    ENCODING_STANDARD,
    FILE_OPEN_WRITE,
    EXTENSION_TXT,
)

FOLDER_OUTPUT = os.getcwd() + "/google_translate_pdfs/data/output/"


def write_file_text_to_txt(original_file_name, text):
    name, _ = os.path.splitext(original_file_name)
    with open(
            FOLDER_OUTPUT + name + EXTENSION_TXT,
            FILE_OPEN_WRITE,
            encoding=ENCODING_STANDARD,
    ) as text_file:
        text_file.writelines(text)
