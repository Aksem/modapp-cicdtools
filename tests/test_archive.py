import zipfile
from pathlib import Path

import pytest
from pytest_mock import MockerFixture
from pytest_unordered import unordered

from modapp_cicdtools.archive import archive_to_zip


def test__file_not_found_error_if_input_not_exists(tmp_path: Path):
    unexisting_input = tmp_path / 'unexisting_dir'
    output = tmp_path / 'result_archive.zip'

    with pytest.raises(FileNotFoundError, match=f"File or directory '{unexisting_input}' doesn't exist"):
        archive_to_zip(path=unexisting_input, output=output)


def test__print_failure_if_input_not_exists(tmp_path: Path, mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")
    unexisting_input = tmp_path / 'unexisting_dir'
    output = tmp_path / 'result_archive.zip'

    with pytest.raises(FileNotFoundError):
        archive_to_zip(path=unexisting_input, output=output, print_on_failure='Archiving failed!')
    
    mock_print.assert_called_once_with("Archiving failed!")


def test__file_not_found_error_if_output_dir_not_exists(tmp_path: Path):
    input_filepath = tmp_path / 'file_to_archive.txt'
    input_filepath.touch()
    output = tmp_path / 'unexisting_dir' / 'result_archive.zip'

    with pytest.raises(FileNotFoundError, match=f"Output directory '{output.parent}' doesn't exist"):
        archive_to_zip(path=input_filepath, output=output)


def test__print_on_failure_if_output_dir_not_exists(tmp_path: Path, mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")
    input_filepath = tmp_path / 'file_to_archive.txt'
    input_filepath.touch()
    output = tmp_path / 'unexisting_dir' / 'result_archive.zip'

    with pytest.raises(FileNotFoundError):
        archive_to_zip(path=input_filepath, output=output, print_on_failure="Archiving failed!")
    
    mock_print.assert_called_once_with("Archiving failed!")


def test__archive_input_file_to_zip(tmp_path: Path):
    # create 2 files to check that only 1 is archived
    input_filepath = tmp_path / 'file_to_archive.txt'
    input_filepath.touch()
    file_not_to_archive = tmp_path / 'file_not_to_archive.txt'
    file_not_to_archive.touch()
    output = tmp_path / 'result_archive.zip'

    archive_to_zip(path=input_filepath, output=output)

    assert output.exists()
    dir_with_extracted = tmp_path / 'extracted'
    dir_with_extracted.mkdir()
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(dir_with_extracted)
    assert list(dir_with_extracted.rglob('*')) == [dir_with_extracted / 'file_to_archive.txt']


def test__print_on_success_archive_input_file_to_zip(tmp_path: Path, mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")
    input_filepath = tmp_path / 'file_to_archive.txt'
    input_filepath.touch()
    output = tmp_path / 'result_archive.zip'

    archive_to_zip(path=input_filepath, output=output, print_on_success='Archiving successful!')

    mock_print.assert_called_once_with("Archiving successful!")


def test__archive_whole_dir_to_zip(tmp_path: Path):
    # create 2 directories to check that only 1 is archived
    input_dir = tmp_path / 'dir_to_archive'
    input_dir.mkdir()
    for filename in ['file1.txt', 'file2.txt']:
        (input_dir / filename).touch()

    dir_not_to_archive = tmp_path / 'dir_not_to_archive'
    dir_not_to_archive.mkdir()
    for filename in ['file1_not_archive.txt', 'file2_not_archive.txt']:
        (dir_not_to_archive / filename).touch()
    output = tmp_path / 'result_archive.zip'

    archive_to_zip(path=input_dir, output=output)

    assert output.exists()
    dir_with_extracted = tmp_path / 'extracted'
    dir_with_extracted.mkdir()
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(dir_with_extracted)
    assert list(dir_with_extracted.rglob('*')) == unordered([dir_with_extracted / input_dir.name, dir_with_extracted / input_dir.name / 'file1.txt', dir_with_extracted / input_dir.name / 'file2.txt'])


def test__print_on_success_archive_whole_dir_to_zip(tmp_path: Path, mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")
    input_dir = tmp_path / 'dir_to_archive'
    input_dir.mkdir()
    output = tmp_path / 'result_archive.zip'

    archive_to_zip(path=input_dir, output=output, print_on_success='Archiving successful!')

    mock_print.assert_called_once_with("Archiving successful!")


def test__archive_dir_content_to_zip(tmp_path: Path):
    # create 2 directories to check that only 1 is archived
    input_dir = tmp_path / 'dir_to_archive'
    input_dir.mkdir()
    for filename in ['file1.txt', 'file2.txt']:
        (input_dir / filename).touch()

    dir_not_to_archive = tmp_path / 'dir_not_to_archive'
    dir_not_to_archive.mkdir()
    for filename in ['file1_not_archive.txt', 'file2_not_archive.txt']:
        (dir_not_to_archive / filename).touch()
    output = tmp_path / 'result_archive.zip'

    archive_to_zip(path=input_dir, output=output, only_content=True)

    assert output.exists()
    dir_with_extracted = tmp_path / 'extracted'
    dir_with_extracted.mkdir()
    with zipfile.ZipFile(output, 'r') as zip_ref:
        zip_ref.extractall(dir_with_extracted)
    assert list(dir_with_extracted.rglob('*')) == unordered([dir_with_extracted / 'file1.txt', dir_with_extracted / 'file2.txt'])



def test__print_on_success_archive_dir_content_to_zip(tmp_path: Path, mocker: MockerFixture):
    mock_print = mocker.patch("builtins.print")
    input_dir = tmp_path / 'dir_to_archive'
    input_dir.mkdir()
    output = tmp_path / 'result_archive.zip'
    
    archive_to_zip(path=input_dir, output=output, only_content=True, print_on_success="Archiving of directory content successful!")
    
    mock_print.assert_called_once_with("Archiving of directory content successful!")
