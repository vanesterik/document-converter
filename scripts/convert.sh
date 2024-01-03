#!/bin/zsh

# Set working directory to root
cd "$(dirname "$0")/.."

# Exit on error
set -e

# Set various path variables
BIB_DIR="./bibliography"
INPUT_DIR="./input"
OUTPUT_DIR="./output"
TEMPLATE_DIR="./templates"

# Check if references.bib exists
if [ ! -f $BIB_DIR/references.bib ]; then

  # Convert markdown files without bibliography
  for file in $INPUT_DIR/*.md; do
    # Define filename without extension
    filename=$(basename "$file" .md)
    # Convert markdown to pdf
    pandoc $file \
      --citeproc \
      --listings \
      --output $OUTPUT_DIR/${filename}.pdf \
      --template $TEMPLATE_DIR/template.tex
  done

  # Exit script
  exit 0
fi

# Convert markdown files with bibliography
for file in $INPUT_DIR/*.md; do
  # Define filename without extension
  filename=$(basename "$file" .md)
  # Convert markdown to pdf
  pandoc $file \
    --bibliography $BIB_DIR/references.bib \
    --citeproc \
    --listings \
    --output $OUTPUT_DIR/${filename}.pdf \
    --template $TEMPLATE_DIR/template.tex
done

# Check if --watch flag is set and watch for changes in input path
if [ "$1" = "--watch" ]; then
  # Watch for changes in markdown files
  fswatch -o $INPUT_DIR/*.md | xargs -n1 -I{} ./scripts/convert.sh
fi
