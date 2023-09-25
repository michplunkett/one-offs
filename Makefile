# Here is some general information on Makefile's so that you can grow this out:
# https://www.gnu.org/software/make/manual/html_node/Introduction.html

.PHONY: lint
lint:
	isort pdf_parser/ google_translate_pdfs/ geocode_verifier/ util/
	black pdf_parser/ google_translate_pdfs/ geocode_verifier/ util/ **/*.ipynb
	ruff pdf_parser/ google_translate_pdfs/ geocode_verifier/ util/

# One-off run commands
.PHONY: translate
translate:
	python -m google_translate_pdfs --source=$(source) --target=$(target)

.PHONY: parse-pdf
parse-pdf:
	python -m pdf_parser

.PHONY: verify-geocodes
verify-geocodes:
	python -m geocode_verifier
