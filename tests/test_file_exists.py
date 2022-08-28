import re
from pathlib import Path

import pytest
from pytest_mock import MockerFixture

from modapp_cicdtools.file_exists import file_exists


def test__file_not_found_error_if_file_not_exists():
    unexisting_file = Path('/tmp/linux_build_result')

    with pytest.raises(
        FileNotFoundError,
        match=re.escape(f"File '{unexisting_file}' doesn't exist"),
    ):
        file_exists(filepath=unexisting_file)


def test__prints_failure_if_file_not_found_error(mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")

    with pytest.raises(
        FileNotFoundError
    ):
        file_exists(filepath=Path('/tmp/linux_build_result'), print_on_failure='Linux build file not found')

    mock_print.assert_called_once_with("Linux build file not found")


def test__no_error_if_file_exists(tmp_path: Path):
    linux_file = tmp_path / "linux_file"
    linux_file.touch()

    file_exists(filepath=linux_file)


def test__prints_success_if_file_found(mocker: MockerFixture, tmp_path: Path):
    mock_print = mocker.patch("builtins.print")
    build_file = tmp_path / "linux_build"
    build_file.touch()

    file_exists(filepath=build_file, print_on_success='Linux build successfully created')

    mock_print.assert_called_once_with("Linux build successfully created")
