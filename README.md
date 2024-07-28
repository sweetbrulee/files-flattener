# Files Flattener

This repository contains implementations for recursively reading all files in a specified directory and outputting their filenames and contents to a specified output file.

- [Why do I need this?](#why-do-i-need-this)
- [Example](#example)
- [Getting Started](#getting-started)
  - [Usage](#usage)
  - [Development](#development)
- [TODO](#todo)
- [License](#license)

## Why do I need this?

Imagine you are working on a project and need to share the project structure and file contents with a collaborator or an **AI platform** for analysis. Instead of manually copying and pasting each file's content, you can use the files_flattener.py script to generate a single file with all the necessary information. This consolidated file can then be easily shared, ensuring that the recipient has all the context needed to understand the project.

## Example

Assume you have the following directory structure:

```
|
|--folder1
|  |--file1.txt
|  |--file2.txt
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

### Usage

1. Ensure you have Python installed on your system.
2. Install the package using pip:
   ```sh
   pip install files_flattener
   ```
3. Run the command:

   ```sh
   flt --help
   ```

   To see the help message.

### Development

#### Install the required dependencies

```sh
pip install -r requirements.txt
```

#### Run the CLI locally

```sh
python -m files_flattener.cli
```

#### Run the tests

```sh
pytest tests/
```

#### Build the package

Ensure `wheel` is installed:

```sh
pip install wheel
```

Generate the distribution files:

```sh
. scripts/build.sh
```

#### Publish the package to PyPI

Install `twine` if you haven't already:

```sh
pip install twine
```

Upload the distribution files to PyPI:

```sh
. scripts/upload.sh
```

## TODO

### 0.2

- [ ] refactor: Use click package to implement the CLI.
- [ ] feat: Add --dry-run mode to preview the output before writing to the file.
- [ ] feat: Use pipeline to output the content instead of typing output file path.

### 0.3

- [ ] feat: Add --file-type="xx;xx;..." options to include or exclude file types. For the filename extension, use the dot prefix e.g. include python files (.py), exclude markdown files (.md). Use a composable class object to dispach file types.
- [ ] feat: Undecoded files will be automatically skipped.

### 0.4

- [ ] feat: Undecoded files will be automatically skipped. If user have specific decoding provider of the files, use `--config=<config json file path>`

  - `config.json` example:

  ```json
  {
    [...]
    "decoder": [
      {
        "name": "PNG decoding method", // optional
        "fileType": ".png",
        "cwd": "...", // context
        "cmd": "png-decoder ${file} --only-metadata"
      },
      [...]
    ],
    [...]
  }
  ```

## License

This project is licensed under the MIT License.
