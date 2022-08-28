"""Test run tool."""
from pathlib import Path
from typing import Optional

from command_runner import command_runner


class CommandExecutionError(Exception):
    """Exception when command execution failed."""

    ...


def test_run_command(
    cmd: str,
    timeout: int = 10,
    cwd: Optional[Path] = None,
    print_on_failure: Optional[str] = None,
    print_on_success: Optional[str] = None,
) -> None:
    """Check whether command(e.g. application) starts without errors.

    Args:
        cmd (str): command to execute
        timeout (int): Timeout in seconds. If the command doesn't stop after the given
                                 timeout, it's successfuly running. Defaults to 10.
        cwd (Optional[Path]): Working directory for command execution. Defaults to None
                              (current directory).
        print_on_failure (Optional[str]): Message to print on failure. Defaults to None.
        print_on_success (Optional[str]): Message to print on success. Defaults to None.

    Raises:
        CommandExecutionError: command execution failed
    """
    exit_code, output = command_runner(
        cmd,
        timeout=timeout,
        cwd=cwd,
    )

    if exit_code == -254:
        # command hasn't stopped after `timeout`, assume it was a successful start
        if print_on_success is not None:
            print(print_on_success)
    elif exit_code != 0:
        if print_on_failure is not None:
            print(print_on_failure)
        raise CommandExecutionError(
            f"Command failed to start, exit code {exit_code}, output: {output}"
        )
    else:
        # successfully finished execution before timeout
        if print_on_success is not None:
            print(print_on_success)
