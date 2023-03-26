# Google Translate Script for News Nerdery
It is currently setup so that you can submit a series of documents to the [Google Translate API](https://github.com/googleapis/python-translate) via a Python 🐍 script.

# Steps to run
1. Install the [Poetry](https://github.com/python-poetry/poetry) virtual environment container at the base directory for this repository.
2. Run the `poetry init` command from the base folder of this repository.
3. Set up your GCloud authentication via this set of instructions: [Link](https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0)
4. Put the pdf files you want translated in the `google_translate_pdfs/data/input` folder.
   - The `google_translate_pdfs/data` folder is in the `.gitignore` file, so you don't have to worry about them being potentially leaked into the repository.
5. Run the `make translate` command from the base folder of the repository and your output files will be in the `google_translate_pdfs/data/output` folder.
