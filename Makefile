.DEFAULT_GOAL := lint

.PHONY: env
env:
	uv venv

.PHONY: install
install:
	uv pip install -r pyproject.toml

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
