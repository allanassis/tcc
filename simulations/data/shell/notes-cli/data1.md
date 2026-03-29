# notes-cli

## Overview

`notes-cli` is a fast and lightweight command-line note-taking tool designed to help users quickly create, manage, and search plain text notes. It emphasizes simplicity, speed, and efficiency on the terminal, enabling seamless note management without the overhead of graphical interfaces or complex databases.

### Domain Concepts

- **Notes**: Plain text files representing pieces of information or thoughts, typically stored in a directory structure.
- **Tags**: Keywords or labels attached to notes to categorize and retrieve them easily.
- **Indexing**: Creating an efficient search index over notes for rapid text and tag-based querying.
- **Commands**: The CLI interface exposes commands for creating, listing, searching, and organizing notes.
- **Editor Integration**: Uses the user's environment editor (e.g., `vim`, `nano`) for editing notes.
- **Note Directory**: A designated folder containing all note files.

`notes-cli` aims to improve productivity by offering an intuitive CLI experience that integrates smoothly into terminal workflows.

---

## Installation

### Prerequisites

- Go (version 1.12+ for building from source)
- A Unix-like OS (Linux, macOS); Windows might require WSL or similar.

### Install via release binaries

Download the latest binary from the [GitHub releases](https://github.com/rhysd/notes-cli/releases) page for your platform, and add it to your system's PATH.

### Build from source (requires Go)

```bash
git clone https://github.com/rhysd/notes-cli.git
cd notes-cli
go build
```

Move the output binary to a directory in your PATH:

```bash
mv notes-cli /usr/local/bin/
```

---

## Usage and Examples

`notes-cli` operates primarily through subcommands. Below are typical usage patterns.

### Setting the Notes Directory

By default, `notes-cli` uses a directory called `~/notes`. You can change this by setting the environment variable `NOTES_DIR`:

```bash
export NOTES_DIR=~/my_notes
```

### Create a new note

Create (or edit) a note:

```bash
notes new "My first note"
```

This opens your default editor to enter the note content. The title is taken from the argument.

### List all notes

List all notes with titles and creation dates:

```bash
notes list
```

### Search notes

Search by text across all notes:

```bash
notes search "meeting notes"
```

Search using tags:

```bash
notes search "#todo"
```

### Open an existing note

Open a note by specifying its name:

```bash
notes open "My first note"
```

### Tagging and Reference

Notes can be tagged inline with `#tagname` inside their content. These tags are indexed for faster searching.

### Indexing notes

Create or update the search index for faster queries:

```bash
notes index
```

This operation is usually done automatically but running manually ensures up-to-date search results.

---

## API Reference (CLI Commands)

### `notes new <title>`

Creates a new note with the specified title. Opens a text editor to compose the content.

- Parameters:
  - `<title>`: The title of the new note (string).
- Behavior:
  - Opens the editor defined by the environment variable `EDITOR` or defaults to `vim`.
  - Saves the note file to the notes directory under a sanitized filename derived from the title.

### `notes list`

Lists all notes in the configured notes directory.

- Output:
  - Displays note titles with metadata such as creation and modification timestamps.

### `notes search <query>`

Searches notes for the specified textual query or tag.

- Parameters:
  - `<query>`: Text to search for in note contents; prefix with `#` to search tags.
- Returns:
  - List of notes matching the query sorted by relevance or recency.

### `notes open <title>`

Opens an existing note with the given title in the text editor.

- Parameters:
  - `<title>`: Title of the note to open.

### `notes index`

Updates the search index of all note contents and tags.

- Purpose:
  - Accelerates `search` queries by precomputing an index.
  - Indexing happens automatically on note creation or editing but can be run manually.

### Environment Variables

- `NOTES_DIR`: Path to the notes directory (default: `~/notes`).
- `EDITOR`: Text editor to open notes (default: `vim`).

---

## Best Practices

- Use meaningful titles for notes to improve file organization.
- Add tags within notes to enable effective categorization and retrieval.
- Regularly run `notes index` if you manipulate notes outside `notes-cli`.
- Use a familiar terminal editor for quick editing and integration.
- Backup your notes directory regularly to prevent data loss.

---

## License

`notes-cli` is licensed under the MIT License. See the LICENSE file in the repository for details.

---

For further details and advanced usage, visit the [GitHub repository](https://github.com/rhysd/notes-cli).
