from loguru import logger
from pathlib import Path
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
import click
import subprocess
import time


@click.command()
@click.option("--watch", is_flag=True, help="Watch mode.")
def main(watch: bool) -> None:
    """
    Main function that either watches files or converts files to PDF.

    Args:
        watch (bool): If True, watch files. If False, convert files to PDF.
    """
    if watch:
        watch_files()
    else:
        convert_files_to_pdf()


def watch_files():
    """
    Watch files in the 'input' directory for changes.

    This function sets up a file observer to monitor the 'input' directory for
    any changes. It uses the `Observer` class from the `watchdog` library to
    detect file system events. When a file is created, modified, or deleted in
    the 'input' directory, the corresponding event is handled by the `Handler`
    class.

    Note: This function runs indefinitely until interrupted by a keyboard
    interrupt (Ctrl+C).

    """
    handler = Handler()
    observer = Observer()
    observer.schedule(
        handler,
        Path("input").absolute(),
        recursive=False,
    )

    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()


class Handler(FileSystemEventHandler):
    @staticmethod
    def on_any_event(event):
        """
        Handles any file system event.

        Args:
            event: The file system event.

        Returns:
            None
        """
        if event.is_directory:
            return None

        elif event.event_type == "created":
            convert_files_to_pdf()
        elif event.event_type == "modified":
            convert_files_to_pdf()


def convert_files_to_pdf():
    """
    Converts Markdown files in the 'input' directory to PDF using Pandoc.

    The function takes the following steps: 1. Defines the base path. 2. Defines
    the input and output paths, references file path, and template file path. 3.
    Loops over the Markdown files in the input path and converts them to PDF
    using Pandoc.
       - It uses the specified template file for styling.
       - If a references file exists, it includes it for citation processing.

    Note: Pandoc and its dependencies must be installed for this function to
    work properly.
    """

    base_path = Path()
    input_path = (base_path / "input").absolute()
    output_path = (base_path / "output").absolute()
    references_file = (base_path / "references/references.bib").absolute()
    template_file = (base_path / "templates/template.tex").absolute()

    files = list(input_path.glob("*.md"))
    for file in files:
        logger.info(f"Converting {file.stem} to pdf.")
        command = [
            "pandoc",
            file,
            "--citeproc",
            "--listings",
            f"--output={output_path / f'{file.stem}.pdf'}",
            f"--resource-path={input_path}",
            f"--template={template_file}",
        ]

        if references_file.exists():
            command.append(f"--bibliography={references_file}")

        subprocess.run(command, check=True)


if __name__ == "__main__":
    main()
