default: lint

.PHONY: env
env:
	uv venv

.PHONY: lint
lint:
	uv run pre-commit run --all-files

# One-off run commands
.PHONY: translate
translate:
	uv run python -m google_translate_pdfs --source=$(source) --target=$(target)

.PHONY: parse-pdf
parse-pdf:
	uv run python -m pdf_parser

.PHONY: verify-geocodes
verify-geocodes:
	uv run python -m geocode_verifier
