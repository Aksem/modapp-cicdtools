"""file_exists tool.

Cross-platform tool to check whether file exists.
"""
from pathlib import Path
from typing import Optional

from loguru import logger


def file_exists(
    filepath: Path,
    print_on_failure: Optional[str] = None,
    print_on_success: Optional[str] = None,
) -> None:
    """Cross-platform check whether file exists.

    Args:
        filepath (Path): Path to file.
        print_on_failure (Optional[str]): Message to print on failure. Defaults to None.
        print_on_success (Optional[str]): Message to print on success. Defaults to None.

    Raises:
        FileNotFoundError: file not found
    """
    if filepath.exists():
        if print_on_success is not None:
            print(print_on_success)
        logger.info(f"File '{filepath}' exists")
    else:
        if print_on_failure is not None:
            print(print_on_failure)
        raise FileNotFoundError(f"File '{filepath}' doesn't exist")
