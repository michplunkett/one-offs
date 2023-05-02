# One-off Monorepo

This repository will house any one-off side projects I create on behalf of others or small scripts I write to accomplish x or y tasks.

## General steps to run a module in this repository
1. Install [`tesseract`](https://github.com/tesseract-ocr/tesseract).
   - To install `tesseract` on a mac, you can run the following command: `brew install tesseract`
   - To install `tesseract` on any other operating systems, please reference [this document.](https://tesseract-ocr.github.io/tessdoc/Installation.html)
2. Install the [Poetry](https://github.com/python-poetry/poetry) virtual environment container at the base directory for this repository.
3. Run the `poetry init` command from the base folder of this repository.

## Use the Google Translate API to translate a set of PDFs
The `google_translate_pdfs` package translates all PDFs in the `google_translate_pdfs/data/input` folder.\
To run it, run this command: `make translate source=[source_lang] target=[target_lang]`
   - The source and target language must be valid [`ISO 639-1` language codes](https://www.loc.gov/standards/iso639-2/php/code_list.php) values.
   - Example: `make translate source=fr target=en`

### Steps to run
1. Set up your GCloud authentication via this set of instructions: [Link](https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0)
   - Run the `gcloud auth application-default login` command to save the credentials for your project to your computer.
2. Put the pdf files you want translated in the `google_translate_pdfs/data/input` folder.
   - The `google_translate_pdfs/data` folder is in the `.gitignore` file, so you don't have to worry about any files being potentially leaked into the repository.
3. Run the `make translate` command from the base folder of the repository and your output files will be in the `google_translate_pdfs/data/output` folder.

## Use the PDF-Parser to parse your PDFs into txt files
The `pdf_parser` package translates all PDFs in the `pdf_parser/data/input` folder.\
To run it, run this command: `make parse-pdf`

### Steps to run
1. Put the PDF files you want parsed in the `pdf_parser/data/input` folder.
   - The `pdf_parser/data` folder is in the `.gitignore` file, so you don't have to worry about any files being potentially leaked into the repository.
2. Run the `make parse-pdf` command from the base folder of the repository and your output files will be in the `pdf_parser/data/output` folder.


## Use the Geocode Verifier to verify the addresses in your CSVs
The `geocode_verifier` package translates all CSVs in the `geocode_verifier/data/input` folder.\
To run it, run this command: `make verify-geocodes`

### Steps to run
1. Set up your GCloud authentication via this set of instructions: [Link](https://codelabs.developers.google.com/codelabs/cloud-translation-python3#0)
   - Run the `gcloud auth application-default login` command to save the credentials for your project to your computer.
2. Put the CSV files you want parsed in the `geocode_verifier/data/input` folder.
   - The `geocode_verifier/data` folder is in the `.gitignore` file, so you don't have to worry about any files being potentially leaked into the repository.
3. Run the `make verify-geocodes` command from the base folder of the repository and your output files will be in the `geocode_verifier/data/output` folder.

### Needed headers and more general things

|  id  | address_number | address | city | zipcode | state |
| :--: | :------------: | :-----: | :--: | :-----: | :---: |

- `city` will be defaulted to `Chicago` if the key is not present.
- `state` will be defaulted to `IL` if the key is not present.
- All addresses are presumed to be in the United States.
