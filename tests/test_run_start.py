from pathlib import Path

import pytest
from pytest_mock import MockerFixture

# rename, because pytest recognizes it as test
from modapp_cicdtools.test_run import test_run_command as run_command, CommandExecutionError


@pytest.fixture
def invalid_program_path(tmp_path: Path):
    program_path = tmp_path / 'invalid_program.py'
    program_path.write_text("print(')")
    return program_path


def test__command_execution_error_if_fails_on_start(invalid_program_path: Path):
    with pytest.raises(CommandExecutionError, match=f'Command failed to start, exit code 1, output:   File "{invalid_program_path}", line 1'):
        run_command(cmd=f"python {str(invalid_program_path)}")


def test__prints_failure_if_fails_on_start(invalid_program_path: Path, mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")

    with pytest.raises(CommandExecutionError):
        run_command(cmd=f"python {str(invalid_program_path)}", print_on_failure="Invalid program has failed")

    mock_print.assert_called_once_with("Invalid program has failed")


def test__success_if_starts_with_return_status_zero():
    run_command(cmd="python -c \"print('hello')\"")


def test__prints_success_if_starts_with_return_status_zero(mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")

    run_command(cmd="python -c \"print('hello')\"", print_on_success="Successfully run!")

    mock_print.assert_called_once_with("Successfully run!")


def test__success_if_timeout():
    run_command(cmd="python -c 'import time; time.sleep(2)'", timeout=1)


def test__prints_success_if_timeout(mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")

    run_command(cmd="python -c 'import time; time.sleep(2)'", timeout=1, print_on_success="Timeout works as expected")

    mock_print.assert_called_once_with("Timeout works as expected")
