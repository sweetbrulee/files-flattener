from .logger import logger_instance as logger

__all__ = ["logger"]

USAGE = """
Usage: flt <directory> <output_file> [<ignore_file>]

Parameters:
  <directory>    : The path of the directory containing the files to be flattened.
  <output_file>  : The path of the output file where the contents of the files will be written.
  [<ignore_file>]: (Optional) The path to a file containing patterns of files to ignore.
                   If not provided, the script will look for a '.ignore' file in the specified directory.
                   If the '.ignore' file is not found, no files will be ignored.
"""


def print_usage(handler=logger.info):
    handler(USAGE)
