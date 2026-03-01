# notes-cli

## Overview

`notes-cli` is a simple and flexible command-line note-taking tool designed for quickly managing plain text notes. It allows users to create, organize, and retrieve notes efficiently from the terminal, without the overhead of complex note-taking applications. The tool focuses on minimalism and productivity, using a directory of text files as its note repository.

### Domain Concepts

- **Notes Repository**: A directory containing individual plain-text note files.
- **Note Files**: Text files representing individual notes identified by unique filenames.
- **Tagging and Searching**: Notes can include tags or keywords for quick searching and filtering.
- **Command-line Interface (CLI)**: User interacts with `notes-cli` through terminal commands to perform note operations.

The tool models the domain of personal note management with a focus on fast access and simple text storage.

---

## Installation

`notes-cli` is implemented in Rust and distributed as a binary.

### Prerequisites

- Rust toolchain for building from source (optional).
- Or download precompiled binaries or install via package managers if available.

### Installing from source

1. Clone the repository:

```bash
git clone https://github.com/rhysd/notes-cli.git
cd notes-cli
```

2. Build the binary using Cargo:

```bash
cargo build --release
```

3. The compiled binary will be in `target/release/notes`.

### Installing via Homebrew (macOS)

```bash
brew install rhysd/tap/notes
```

### Usage requires having a directory to store notes:

Create a directory to use as your notes repository:

```bash
mkdir ~/notes
```

---

## Usage and Examples

`notes-cli` provides various commands to manage notes. Below are some common usage examples.

### Initialize a notes repository

Set the environment variable `NOTES_DIR` to point to your notes directory:

```bash
export NOTES_DIR=~/notes
```

or specify the directory with the `-d` option:

```bash
notes -d ~/notes <command> ...
```

### Create a new note

```bash
notes new "Todo for project"
```

This creates a new note file with a timestamp-based filename containing the note text "Todo for project" opened for editing.

### Edit an existing note

To edit a note by its filename:

```bash
notes edit 20220414123045.txt
```

This opens the note file in the default text editor.

### List all notes

```bash
notes list
```

This lists all note filenames with their creation dates.

### Search notes by keyword or tag

```bash
notes search "project"
```

Shows notes containing the keyword "project" in their content.

### Delete a note

```bash
notes delete 20220414123045.txt
```

Deletes the specified note file.

### Show note content

```bash
notes show 20220414123045.txt
```

Outputs the content of the note to the terminal.

---

## API Reference

The primary interface to `notes-cli` is via its CLI commands. Below are the main commands (subcommands) with their options and usage.

### `notes new [title]`

Create a new note with an optional title. Opens the editor for entering note content.

- `title` (string, optional): Title or first line of the note.

Returns: Newly created note filename.

---

### `notes edit <filename>`

Edit an existing note by filename.

- `filename` (string): Name of the note file to edit.

Returns: Opens editor and saves changes.

---

### `notes list`

List all notes with metadata like date and title (if any).

Returns: List of note files.

---

### `notes search <query>`

Search for notes containing the query string.

- `query` (string): Keyword or tag to search for.

Returns: List of matching note filenames.

---

### `notes show <filename>`

Show the content of a specific note.

- `filename` (string): Note filename.

Returns: Note content printed to console.

---

### `notes delete <filename>`

Remove a note file.

- `filename` (string): Note filename.

Returns: Deletes the specified note.

---

### Global Options

- `-d`, `--dir <path>`: Specify the notes directory if not using `NOTES_DIR` environment variable.
- `-h`, `--help`: Show usage information.
- `-v`, `--version`: Show version information.

---

## Contributing

Contributions to `notes-cli` are welcome! To contribute:

1. Fork the GitHub repository.
2. Create a feature branch or issue fix branch.
3. Submit a pull request with clear descriptions.
4. Follow coding and commit message conventions.
5. Include tests and documentation updates if applicable.

Please report bugs or feature requests via GitHub issues.

---

## License

`notes-cli` is licensed under the MIT License. See the [LICENSE](https://github.com/rhysd/notes-cli/blob/master/LICENSE) file for details.

---

## Contact

- Repository: [https://github.com/rhysd/notes-cli](https://github.com/rhysd/notes-cli)
- Issues: Use GitHub Issues on the repository page for bug reports and feature requests.
- Author: Rhysd (https://github.com/rhysd)
