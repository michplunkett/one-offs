# Here is some general information on Makefile's so that you can grow this out:
# https://www.gnu.org/software/make/manual/html_node/Introduction.html

.PHONY: lint
lint:
	isort test/ pdf_parser/ google_translate_pdfs/ geocode_verifier/ util/
	black test/ pdf_parser/ google_translate_pdfs/ geocode_verifier/ util/ **/*.ipynb
	ruff test/ pdf_parser/ google_translate_pdfs/ geocode_verifier/ util/

.PHONY: test
test:
	pytest -vs test/

.PHONY: test-and-fail
test-and-fail:
	pytest -vsx test/

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
