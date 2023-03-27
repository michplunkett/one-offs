"""
This file runs the translation process for a set of PDFs housed in the
/data/input folder.
"""

from google_translate_pdfs.file_management import (
    get_file_text,
    get_files_to_translate,
    write_translation_to_csv,
)
from google_translate_pdfs.translation import gcloud_translate
from util.constants import (
    EXTENSION_PDF,
    ISO_LANG_CODE_ENGLISH,
    ISO_LANG_CODE_FRENCH,
)


def main(src_lang, target_lang):
    """
    The process runner for the translation process.

    Inputs:
        src_lang (string): an ISO 639-1 language code for the text's original
            language
        target_language (string): an ISO 639-1 language code for the text's
            target language
    """

    pdf_files = get_files_to_translate(EXTENSION_PDF)
    for file in pdf_files:
        file_text = get_file_text(file)
        filtered_file_text = list(filter(lambda t: t != "", file_text))
        if len(filtered_file_text) > 0:
            print(f"Translating {file}.")
            translated_text = gcloud_translate(src_lang, target_lang, file_text)
            write_translation_to_csv(file, file_text, translated_text)
            print(f"Done writing translated output for {file}.")
        else:
            print(f"There was not any parseable text in this file: {file}")


if __name__ == "__main__":
    main(ISO_LANG_CODE_FRENCH, ISO_LANG_CODE_ENGLISH)
