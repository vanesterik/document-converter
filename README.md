![Scroopy Noopers](./scroopy-noopers.webp)

# Scroopy Noopers

Scroopy Noopers helps you convert Markdown files to PDF format. It is a simple tool that uses Pandoc and LaTeX to convert Markdown files to PDF format. It is designed to be used in watch mode, so that you can focus on writing your paper and not worry about converting it to PDF format.

## Rationale

I created this project because I wanted a simple tool that would convert Markdown files to PDF format. I wanted to be able to focus on writing my paper and not worry about converting it to PDF format. I also wanted to be able to use Pandoc and LaTeX to convert Markdown files to PDF format.

## Name

Scroopy Noopers is a scientist and outcast on the celestial dwarf Pluto. He first appeared in [Something Ricked This Way Comes](https://www.imdb.com/title/tt3333840/?ref_=ttep_ep9). The fact that he is a scientist rather fits well with the scientific nature of this project. The featured episode is one of my favorites and I also think it is funny to say **Scroopy Noopers**.

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
