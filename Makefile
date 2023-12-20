.PHONY: test mandoc-serve mandoc apidoc

test:
	pytest tests/ funcpipe/

cov:
	python -m http.server -d .html-coverage

mandoc-serve: mandoc
	mkdocs serve

mandoc:
	rm docs/index.md
	cp README.md docs/index.md
	mkdocs build

apidoc-serve: apidoc
	python -m http.server -d docs/apidoc

apidoc:
	rm -rf ./docs/apidoc
	pdoc funcpipe -o ./docs/apidoc --docformat google
