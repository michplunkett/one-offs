"""
This file houses the Google Translate API logic.
"""

import six
from google.cloud import translate_v2 as translate
from util.constants import ENCODING_STANDARD


def gcloud_translate(src_lang, target_lang, text):
    """
    Gets the Google Translate API client.
    Inputs:
        src_lang (string): an ISO 639-1 language code
        target_language (string): an ISO 639-1 language code
        text (list of strings): the string that is to be translated

    Returns:
        The translated text.
    """

    translate_client = translate.Client()

    if isinstance(text, six.binary_type):
        text = text.decode(ENCODING_STANDARD)

    results = []

    for t in text:
        if t == "":
            results.append("")
            continue

        resp = translate_client.translate(
            t, source_language=src_lang, target_language=target_lang
        )
        if resp["translatedText"]:
            results.append(resp["translatedText"])

    return results
