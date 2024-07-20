## Files Flattener

This repository contains implementations for recursively reading all files in a specified directory and outputting their filenames and contents to a specified output file.

- [Getting Started](#getting-started)
  - [Python](#python)

## Why do I need this?

Imagine you are working on a project and need to share the project structure and file contents with a collaborator or an **AI platform** for analysis. Instead of manually copying and pasting each file's content, you can use the files_flattener.py script to generate a single file with all the necessary information. This consolidated file can then be easily shared, ensuring that the recipient has all the context needed to understand the project.

### Example

Assume you have the following directory structure:

```

|
|--folder1
| |--file1.txt
| |--file2.txt
|--file3.txt

```

And you have an `.ignore` file in the root directory with the following content:

```

folder1/file2.txt

# Exclude itself

.ignore

```

Running the implementation will process the files, ignoring `folder1/file2.txt` and `.ignore` itself as specified in the `.ignore` file. The output file will contain the contents of the remaining files in the following format:

```

**folder1/file1.txt:**

[...file1.txt's content...]

**file3.txt:**

[...file3.txt's content...]

```

## Getting Started

### Python

#### Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:

   ```sh
   pip install -r requirements.txt
   ```

3. Run the script using the command:

   ```sh
   python files_flattener.py <directory> <output_file> [<ignore_file>]
   ```

#### Parameters

- `<directory>`: The path of the directory containing the files to be flattened.
- `<output_file>`: The path of the output file where the contents of the files will be written.
- `[<ignore_file>]`: (Optional) The path to a file containing patterns of files to ignore. If not provided, the script will look for a '.ignore' file in the specified directory. If the '.ignore' file is not found, no files will be ignored.

## TODO

- [ ] Add dry-run mode to preview the output before writing to the file.
- [ ] Make a Node library version.
- [ ] Make a web app based on Vue3.
- [x] Use `.ignore` to exclude or include files for flattening.

## License

This project is licensed under the MIT License.
