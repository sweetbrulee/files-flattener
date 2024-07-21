import os
import sys
import pathspec
from concurrent.futures import ThreadPoolExecutor
from .directory_handler import (
    DirectoryHandlerFactory,
    LocalDirectoryHandler,
    RemoteRepositoryHandler,
)
from .common import logger

USAGE = """
Usage: flt <identifier> <output_file> [<ignore_file>]

Parameters:
  <identifier>   : The path of the local directory or the URL of the remote repository containing the files to be flattened.
  <output_file>  : The path of the output file where the contents of the files will be written.
  [<ignore_file>]: (Optional) The path to a file containing patterns of files to ignore.
                   If not provided, the script will look for a '.ignore' file in the specified directory.
                   If the '.ignore' file is not found, no files will be ignored.
"""


def get_spec(ignore_file):
    with open(ignore_file, "r", encoding="utf-8") as f:
        ignore_patterns = f.read().splitlines()
    return pathspec.PathSpec.from_lines(
        pathspec.patterns.GitWildMatchPattern, ignore_patterns
    )


def list_files(directory, ignore_file=None):
    handler = DirectoryHandlerFactory.get_handler(directory)
    handler.prepare()

    files_list = []
    spec = None

    if ignore_file:
        # If the ignore file not exists, raise an error
        if not os.path.exists(ignore_file):
            logger.error(f"Ignore file {ignore_file} does not exist.")
            logger.info(USAGE)
            sys.exit(1)

        # Ignore file is valid, get the patterns
        spec = get_spec(ignore_file)
    elif os.path.exists(os.path.join(handler.local_directory, ".ignore")):
        # If .ignore file is found in the directory and valid, get the patterns
        spec = get_spec(os.path.join(handler.local_directory, ".ignore"))

    # Else, no ignore file is found, no files will be ignored

    # Walk through the directory and list all files
    for root, _, files in os.walk(handler.local_directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, handler.local_directory)
            if spec and spec.match_file(relative_path):
                continue
            files_list.append(relative_path)

    return files_list, handler


def read_file_content(file_path):
    with open(file_path, "r", encoding="utf-8") as infile:
        return infile.read()


def write_files_to_output(
    handler: LocalDirectoryHandler | RemoteRepositoryHandler, output_file, files_list
):
    try:
        with open(output_file, "w", encoding="utf-8") as outfile:
            # Use multiple threads to read file contents
            with ThreadPoolExecutor() as executor:
                future_to_file = {
                    executor.submit(
                        read_file_content,
                        os.path.join(handler.local_directory, relative_path),
                    ): relative_path
                    for relative_path in files_list
                }

                for future in future_to_file:
                    relative_path = future_to_file[future]
                    try:
                        content = future.result()
                        outfile.write(f"**{relative_path}:**\n\n")
                        outfile.write(content)
                        outfile.write("\n\n")
                    except Exception as exc:
                        logger.critical(f"Error reading file {relative_path}: {exc}")
                        # Delete output file and exit
                        os.remove(output_file)
                        sys.exit(1)
    finally:
        # Clean up the temporary directory if it was used
        if isinstance(handler, RemoteRepositoryHandler):
            handler.remove_local_directory()
