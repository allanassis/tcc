# notes-cli

## Overview

`notes-cli` is a command-line tool designed for managing plain text notes efficiently directly from the terminal. It allows users to quickly create, search, list, and open notes organized in a simple directory structure. The tool emphasizes minimalism, speed, and ease of use by leveraging standard text files and powerful command-line utilities, making it suitable for users who prefer a keyboard-driven workflow and plain text note-taking.

### Domain Concepts

- **Notes Directory**: A folder where all notes are stored as individual text files.
- **Note Files**: Plain text files representing individual notes, typically with `.txt` or user-defined extensions.
- **Note Metadata**: Basic metadata such as creation time and modification time associated with each note file.
- **Search & Filter**: Mechanisms to quickly find notes by keywords or patterns.
- **Note Actions**: Creating new notes, listing notes, opening existing notes in an editor, and deleting notes.

---

## Installation

### Prerequisites

- Go programming environment (version 1.16 or higher recommended).

### Installation from source

Clone the repository and build the binary:

```bash
git clone https://github.com/rhysd/notes-cli.git
cd notes-cli
go build
```

This produces an executable `notes-cli` in the current directory.

### Installing using prebuilt binaries

Prebuilt binaries for various platforms may be available under the [releases](https://github.com/rhysd/notes-cli/releases) section on GitHub. Download and place the binary in your system PATH.

---

## Usage and Examples

Once installed, `notes-cli` can be used via the command line to manipulate notes.

### Setting Notes Directory

By default, notes are stored in the directory specified by the environment variable `NOTES_DIR`. If not set, it uses `~/notes`.

Example to set environment variable:

```bash
export NOTES_DIR=~/my_notes
```

### Creating a New Note

Create a new note with a title. This opens the note in the configured editor (defaults to `$EDITOR` or `vi`):

```bash
notes-cli new "My First Note"
```

This creates a file named like the note title, e.g., `My First Note.txt` in the notes directory and opens it for editing.

### Listing Notes

List all note titles:

```bash
notes-cli list
```

Output Example:

```
My First Note.txt
Meeting Notes.txt
Project Ideas.txt
```

### Searching Notes

Search note contents for a keyword, displaying matching note names:

```bash
notes-cli search keyword
```

### Opening a Note

Open an existing note by title in the editor:

```bash
notes-cli open "Meeting Notes"
```

If multiple matches are found, it prompts to select.

### Deleting a Note

Remove a note by title:

```bash
notes-cli delete "Project Ideas"
```

---

## API Reference

The tool mainly works through CLI commands with the following primary commands:

### `new <title>`

- Creates a new note with the specified `<title>`.
- Opens the note with the default editor.
- If a note with the same name exists, the user is prompted about overwrite.

### `list`

- Lists all note files in the notes directory with their filenames.

### `search <keyword>`

- Searches all notes for the given keyword.
- Outputs note files containing the keyword.

### `open <title>`

- Opens the note matching the `<title>` for editing.
- If multiple matches, prompts selection.
- Uses `$EDITOR` environment variable or defaults to `vi`.

### `delete <title>`

- Deletes the note matching the `<title>`.
- Asks for confirmation by default.

### Common Options

- `-h, --help`: Show help information.
- `--version`: Show current version of notes-cli.

---

## License

`notes-cli` is licensed under the MIT License. See the [LICENSE](https://github.com/rhysd/notes-cli/blob/master/LICENSE) file for details.
