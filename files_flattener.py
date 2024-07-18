import os
import sys
import pathspec

USAGE = "Usage: python files_flattener.py <directory> <output_file> [<ignore_file>]"


def load_ignore_patterns(ignore_file):
    with open(ignore_file, "r", encoding="utf-8") as f:
        patterns = f.read().splitlines()
    return patterns


def list_files(directory, ignore_file):
    files_list = []
    if ignore_file:
        ignore_patterns = load_ignore_patterns(ignore_file)
        spec = pathspec.PathSpec.from_lines(
            pathspec.patterns.GitWildMatchPattern, ignore_patterns
        )
    else:
        spec = None

    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, directory)
            if spec and spec.match_file(relative_path):
                continue
            files_list.append(relative_path)

    return files_list


def write_files_to_output(directory, output_file, files_list):
    with open(output_file, "w", encoding="utf-8") as outfile:
        for relative_path in files_list:
            file_path = os.path.join(directory, relative_path)
            with open(file_path, "r", encoding="utf-8") as infile:
                outfile.write(f"**{relative_path}:**\n\n")
                outfile.write(infile.read())
                outfile.write("\n\n")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(USAGE)
        sys.exit(1)

    directory = sys.argv[1]
    output_file = sys.argv[2]
    ignore_file = (
        sys.argv[3] if len(sys.argv) > 3 else os.path.join(directory, ".ignore")
    )

    if not os.path.exists(ignore_file):
        print(f"Ignore file {ignore_file} does not exist.")
        print("Specify a valid ignore file or create a .ignore file in the directory.")
        print(USAGE)
        sys.exit(1)

    files_list = list_files(directory, ignore_file)

    print("Files to be processed:")
    for file in files_list:
        print(file)

    write_files_to_output(directory, output_file, files_list)
    print(f"All files have been successfully written to {output_file}")
