# Document Converter

This is a simple document converter that converts a document from markdown format to pdf by making use of a LaTeX template. It is written in [Z shell](https://en.wikipedia.org/wiki/Z_shell) and uses the [Pandoc](https://pandoc.org/) library to do the actual conversion.

## System Requirements

This project assumes that your system is running macOS and has the following programs installed:

- [fswatch](https://emcrisostomo.github.io/fswatch/)
- [MacTeX](https://www.tug.org/mactex/) (or any other LaTeX distribution)
- [Pandoc](https://pandoc.org/)

All of these can be installed using [Homebrew](https://brew.sh/).

## Structure

The project is structured as follows:

```
project/
├── bibliography/
│   └── references.bib
├── input/
│   ├── file1.md
│   ├── file2.md
│   └── ...
├── output/
│   ├── file1.pdf
│   ├── file2.pdf
│   └── ...
└── templates/
    └── template.tex
```

Just add your markdown files to the `input` directory and run the converter. The converted pdf files will be placed in the `output` directory.

## Usage

To use the converter in watch mode, run the following command in the terminal:

```bash
make watch
```

This will watch for changes in the `markdown_files` directory and convert the files to pdf whenever a change is detected.

To convert the files once, run the following command in the terminal:

```bash
make convert
```

## Gotchas

- The `bibliography` folder is empty and will be ignored if no bibliography is used. If you want to use a bibliography, place the `.bib` file in the `bibliography` folder and name it `references.bib`.

- The image paths in the markdown files are relative to the `input` directory. If you want to use images, place them in the `input` directory and reference them in the markdown files using the relative path.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
