"""Archive tool."""
from pathlib import Path
from shutil import copyfile, copytree, make_archive, move
from tempfile import TemporaryDirectory
from typing import Optional

from loguru import logger


def _make_archive_to_output(
    base_name: str,
    format: str,
    root_dir: Path,
    base_dir: Path,
    output_filepath: Path,
    print_on_success: Optional[str] = None,
) -> None:
    # make_archive saves archive to current working directory, copy it to output
    archive_path_str = make_archive(
        base_name, format, root_dir, base_dir.relative_to(base_dir)
    )
    move(archive_path_str, output_filepath)
    logger.info(f"Created archive '{archive_path_str}'")
    if print_on_success is not None:
        print(print_on_success)


def archive_to_zip(
    path: Path,
    output: Path,
    only_content: bool = False,
    print_on_failure: Optional[str] = None,
    print_on_success: Optional[str] = None,
) -> None:
    """Archive either directory, directory content or file to a zip archive.

    Args:
        path (Path): full path to file or directory which should be archived
        output (Path): output file (path with filename and extension)
        only_content (bool): archive only content of the directory if `path` is a
                             directory. Defaults to False.
        print_on_failure (Optional[str]): Message to print on failure. Defaults to None.
        print_on_success (Optional[str]): Message to print on success. Defaults to None.

    Raises:
        FileNotFoundError: either input file/directory `path` or output directory doesn't exist
    """
    if not path.exists():
        if print_on_failure is not None:
            print(print_on_failure)
        raise FileNotFoundError(f"File or directory '{path}' doesn't exist")

    if not output.parent.exists():
        if print_on_failure is not None:
            print(print_on_failure)
        raise FileNotFoundError(f"Output directory '{output.parent}' doesn't exist")

    base_name = output.stem
    format = output.suffix[1:]
    if path.is_dir() and only_content:
        root_dir = path
        base_dir = path
        _make_archive_to_output(
            base_name, format, root_dir, base_dir, output, print_on_success
        )
    else:
        # to avoid archiving other files and directories in the same directory, copy input
        # to temporary directory and archive its content
        with TemporaryDirectory() as tmpdirname:
            tmpdir_path = Path(tmpdirname)
            if path.is_dir():
                copytree(path, tmpdir_path / path.name)
            else:
                copyfile(path, tmpdir_path / path.name)

            _make_archive_to_output(
                base_name, format, tmpdir_path, tmpdir_path, output, print_on_success
            )
