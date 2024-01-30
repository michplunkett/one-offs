default: lint

.PHONY: lint
lint:
	pre-commit run --all-files

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
