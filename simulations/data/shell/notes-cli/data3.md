# notes-cli

## Overview

`notes-cli` is a simple and efficient command-line tool designed for managing plain text notes. Its main purpose is to provide a minimalistic, fast, and easy way to create, search, and manage notes within a terminal environment. It is particularly useful for developers and users who want to keep organized text-based notes without the overhead of complex note-taking applications.

### Domain Concepts

- **Note**: A plain text file representing a unit of information or thought.
- **Tags**: Keywords associated with notes for easier organization and retrieval.
- **Search**: Querying notes by content or tags using efficient search mechanisms.
- **Note Storage**: Notes are stored as files in a directory structure on disk.
- **Command-line Interface**: Interaction with the tool happens through text commands in a Unix-like terminal.

---

## Installation

`notes-cli` can be installed from source or via package managers if supported.

### Installing from source

1. Clone the repository:

```bash
git clone https://github.com/rhysd/notes-cli.git
cd notes-cli
```

2. Build (if necessary, depending on language/toolchain - typically Rust or other):

For Rust (if notes-cli is a Rust project):

```bash
cargo install --path .
```

Or build and install manually as per language/toolchain instructions.

### Other installation methods

Check the repository README or releases section for pre-built binaries or package manager availability.

---

## Usage and Examples

The main interaction with `notes-cli` happens through various subcommands to create, edit, search, and list notes.

### Basic Commands

- **Create a new note**:

```bash
notes new "note-title"
```

Creates a new note titled "note-title" and opens it for editing.

- **List notes**:

```bash
notes list
```

Lists all saved notes with their titles and metadata.

- **Search notes by keyword**:

```bash
notes search "keyword"
```

Searches all notes containing the keyword.

- **Add tags to a note**:

Tags can be added in the note content or via commands (if supported), allowing categorization.

---

### Example Workflow

1. Create a new note:

```bash
notes new "Meeting Notes"
```

2. Edit the note in the default editor.

3. Search for notes related to "project":

```bash
notes search "project"
```

4. List notes with a specific tag (if tags supported):

```bash
notes list --tag "work"
```

---

## API Reference

`notes-cli` primarily exposes its functionality as CLI commands. The main commands and their options include:

### `notes new <title>`

Creates a new note with the specified title. Opens the note in the configured editor.

- `title` (string): Title of the new note.

### `notes list [--tag <tag>]`

Lists notes. Optionally filters notes by a tag.

- `--tag` (string, optional): Filter notes by the given tag.

### `notes search <query>`

Searches for notes containing the query string.

- `query` (string): The search keyword or phrase.

### `notes edit <note-id>`

Opens an existing note identified by `note-id` in the default editor.

- `note-id` (string or number): Identifier of the note to edit.

### `notes delete <note-id>`

Deletes the specified note.

- `note-id` (string or number): Identifier of the note to delete.

---

## Contributing

Contributions are welcome! To contribute to `notes-cli`:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Make your changes and add tests if applicable.
4. Commit your changes (`git commit -m "Add feature"`).
5. Push to your branch (`git push origin feature-name`).
6. Create a pull request via GitHub.

Please follow the project's coding style and make sure tests pass.

---

## License

`notes-cli` is licensed under the MIT License. See the [LICENSE](https://github.com/rhysd/notes-cli/blob/master/LICENSE) file for details.

---

## Contact

- Repository: [https://github.com/rhysd/notes-cli](https://github.com/rhysd/notes-cli)
- Issues: Use the GitHub Issues page to report bugs or request features.
- Author: Ryuta Hosoya (rhysd)
