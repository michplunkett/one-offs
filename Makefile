# Here is some general information on Makefile's so that you can grow this out:
# https://www.gnu.org/software/make/manual/html_node/Introduction.html

.PHONY: format
format:
	black test/ google_translate_pdfs/ --line-length=80

.PHONY: lint
lint:
	pylint test/ google_translate_pdfs/

.PHONY: test
test:
	pytest -vs test/

.PHONY: test-and-fail
test-and-fail:
	pytest -vsx test/

# One-off run commands
.PHONY: translate
translate:
	python -m google_translate_pdfs
