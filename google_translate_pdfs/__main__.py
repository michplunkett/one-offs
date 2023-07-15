"""
This file runs the translation process for the set of PDFs housed in the
./data/input folder.
"""

import argparse
import os
import sys

from google_translate_pdfs.file_management import write_translation_to_csv
from google_translate_pdfs.translation import gcloud_translate
from util.constants import ISO_LANGUAGES
from util.pdf import get_file_text, get_files

FOLDER_INPUT = os.getcwd() + "/google_translate_pdfs/data/input/"


def main():
    """
    The process runner for the translation process.

    For a list of ISO 639-1, go here:
    https://www.loc.gov/standards/iso639-2/php/code_list.php
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source",
        help="Set the source documents' language",
        type=str,
        default="",
    )

    parser.add_argument(
        "--target",
        help="Set the target translation language",
        type=str,
        default="",
    )

    args = parser.parse_args()

    source_lang = args.source.strip()
    target_lang = args.target.strip()

    if not source_lang or len(source_lang) != 2:
        print(
            "You did not include a source language or you submitted one "
            "that was not two-letters in length."
        )
        sys.exit()

    if not target_lang or len(target_lang) != 2:
        print(
            "You did not include a target language or you submitted one "
            "that was not two-letters in length."
        )
        sys.exit()

    if source_lang not in ISO_LANGUAGES:
        print(f"You submitted a non-ISO 639-1 source language: {source_lang}")
        sys.exit()

    if target_lang not in ISO_LANGUAGES:
        print(f"You submitted a non-ISO 639-1 target language: {target_lang}")
        sys.exit()

    pdf_files = get_files(FOLDER_INPUT)
    for file in pdf_files:
        file_text = get_file_text(file, FOLDER_INPUT)
        filtered_file_text = list(filter(lambda t: t[1] != "", file_text))
        if len(filtered_file_text) > 0:
            print(f"Translating {file}.")
            translated_text = gcloud_translate(
                source_lang, target_lang, [t[1] for t in file_text]
            )
            write_translation_to_csv(file, file_text, translated_text)
            print(f"Done writing translated output for {file}.")
        else:
            print(f"There was not any parseable text in this file: {file}")


if __name__ == "__main__":
    main()
