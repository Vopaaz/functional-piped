.PHONY: test mandoc-serve mandoc apidoc

test:
	pytest tests/ dotmap/

mandoc-serve: apidoc
	mkdocs serve

mandoc: apidoc
	mkdocs build

apidoc:
	rm -rf ./docs/apidoc
	pdoc dotmap -o ./docs/apidoc --docformat google
