"""Pulls the text from the set of PDFs housed in the ./data/input folder."""
import os

from pdf_parser.file_management import write_file_text_to_txt
from util.pdf import get_file_text, get_files

FOLDER_INPUT = os.getcwd() + "/google_translate_pdfs/data/input/"


def main():
    """Parse all .pdf files from the `FOLDER_INPUT` directory."""
    pdf_files = get_files(FOLDER_INPUT)
    for file in pdf_files:
        print(f"Getting text from {file}.")
        file_text = get_file_text(file, FOLDER_INPUT)
        print(f"Done getting text from {file}.")
        filtered_file_text = list(filter(lambda t: t[1] != "", file_text))
        if len(filtered_file_text) > 0:
            write_file_text_to_txt(file, [t[1] for t in file_text])
            print(f"Done writing text output for {file}.")
        else:
            print(f"There was not any parseable text in this file: {file}")


if __name__ == "__main__":
    main()
