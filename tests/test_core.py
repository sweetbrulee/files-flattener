import absimport  # FIRST LINE
import pytest
from files_flattener.core import list_files
from files_flattener.identifier_handler import LocalDirectoryHandler


@pytest.mark.parametrize(
    "identifier, ignore_file, ignored",
    [
        ("tests/testdata/target", None, "folder1/file2.txt"),
        ("tests/testdata/target", "tests/testdata/.ignore", "folder1/file2.txt"),
    ],
)
def test_list_files(identifier, ignore_file, ignored):
    files, handler = list_files(identifier, ignore_file)
    assert isinstance(files, list)
    assert isinstance(handler, LocalDirectoryHandler)
    assert ignored not in files if ignore_file else ignored in files
