![Scroopy Noopers](./scroopy-noopers.webp)

# Scroopy Noopers

I chose to name this project "Scroopy Noopers" because it reflects the scientific nature of the work involved. This decision is influenced by the character Scroopy Noopers, who is depicted as a scientist. The main goal of the project is to convert Markdown files into PDF format, especially focusing on research papers. Writing research papers is inherently a scientific activity, so naming it "Scroopy Noopers" aligns well with the project's theme.

Additionally, my personal fondness for the television series "Rick and Morty" played a role in selecting this name.

## System Requirements

This project assumes that your system is running macOS and has the following programs installed:

- [MacTeX](https://www.tug.org/mactex/) (or any other LaTeX distribution)
- [Pandoc](https://pandoc.org/)

All of these can be installed using [Homebrew](https://brew.sh/).

## Structure

The project is structured as follows:

```
project/
├── references/
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

This will watch for changes in the `input` directory and convert the files to pdf whenever a change is detected.

To convert the files once, run the following command in the terminal:

```bash
make convert
```

## Gotchas

- The `references` folder is empty and will be ignored if no bibliography is used. If you want to use a bibliography, place the `.bib` file in the `references` folder and name it `references.bib`.

- The image paths in the markdown files are relative to the `input` directory. If you want to use images, place them in the `input` directory and reference them in the markdown files using only the filename.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
