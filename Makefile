.PHONY: help clean run watch
DEFAULT_GOAL := help

help:
	@echo "make clean"
	@echo "       clean all files in data/processed except .gitkeep"
	@echo "make convert"
	@echo "       convert all markdown files in input/ to pdf files in output/"
	@echo "make watch"
	@echo "       convert and watch for changes in input/"

clean:
	@echo "cleaning all files in input/ except .gitkeep"
	find input -type f ! -name '.gitkeep' -delete

convert:
	pdm run python run.py

watch:
	pdm run python run.py --watch