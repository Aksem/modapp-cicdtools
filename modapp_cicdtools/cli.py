"""Command-line interface."""
from pathlib import Path
from typing import Optional

import typer

from modapp_cicdtools.archive import archive_to_zip
from modapp_cicdtools.file_exists import file_exists as _file_exists
from modapp_cicdtools.test_run import test_run_command

app = typer.Typer()


@app.command()
def archive(
    path: Path,
    output: Path,
    only_content: bool = False,
    print_on_failure: Optional[str] = None,
    print_on_success: Optional[str] = None,
) -> None:
    """Archive either directory, directory content or file to a zip archive."""
    archive_to_zip(
        path=path,
        output=output,
        only_content=only_content,
        print_on_success=print_on_success,
        print_on_failure=print_on_failure,
    )


@app.command()
def file_exists(
    filepath: Path,
    print_on_failure: Optional[str] = None,
    print_on_success: Optional[str] = None,
) -> None:
    """Cross-platform check whether file exists."""
    _file_exists(
        filepath=filepath,
        print_on_success=print_on_success,
        print_on_failure=print_on_failure,
    )


@app.command()
def test_run(
    command: str,
    timeout: int = 10,
    cwd: Optional[Path] = None,
    print_on_failure: Optional[str] = None,
    print_on_success: Optional[str] = None,
) -> None:
    """Check whether command(e.g. application) starts without errors."""
    test_run_command(
        cmd=command,
        timeout=timeout,
        cwd=cwd,
        print_on_success=print_on_success,
        print_on_failure=print_on_failure,
    )


if __name__ == "__main__":
    app()
