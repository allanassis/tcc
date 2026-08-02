# notes-cli

## Overview

`notes-cli` is a simple and lightweight command-line tool for managing and manipulating personal notes stored as plain text files. It is designed to provide fast and intuitive note-taking, searching, and organizing capabilities directly from the terminal without the need for complex setups or databases. The tool emphasizes ease of use with common file system operations enhanced with note-specific features.

### Domain Concepts

- **Notes as Files:** Individual notes are stored as plain text files in a user-specified directory.
- **Note Searching:** Supports searching notes by keywords or tags.
- **Note Editing:** Launches the user’s preferred terminal editor to create or modify notes.
- **Tagging:** Enables categorizing notes with tags for easier retrieval.
- **Note Listing and Filtering:** Lists notes with optional filters such as by recent activity or tags.
- **Metadata:** Notes can include metadata such as creation date and tags inside the file content.

`notes-cli` models the note-taking domain by treating notes as lightweight text files and providing commands for common workflows like adding, editing, searching, and listing notes with tagging support.

---

## Installation

`notes-cli` is a Go-based application that can be installed easily via precompiled binaries, package managers, or Go tools.

### Using precompiled binaries

Download the latest release from the GitHub repository's [Releases](https://github.com/rhysd/notes-cli/releases) page for your OS and architecture.

Unpack and move executable to a directory in your `PATH`.

### Using Homebrew (macOS / Linux)

```bash
brew install rhysd/tap/notes-cli
```

### Building from source

Prerequisites:

- Go 1.13 or later installed.

```bash
git clone https://github.com/rhysd/notes-cli.git
cd notes-cli
make build
./notes
```

Add the executable `notes` to your system `PATH` for convenience.

---

## Usage and Examples

`notes-cli` uses a command-line interface with subcommands for different operations.

Basic command structure:

```bash
notes [command] [flags]
```

### Common Commands and Usage Patterns

#### Create or Edit a Note

Launches your default editor (configurable via `$EDITOR` environment variable) to create or update a note.

```bash
notes edit mynote
```

If the note `mynote` does not exist, a new file is created.

#### Search Notes

Search notes by text or tag with a fast search engine supporting regex.

```bash
notes search keyword
```

To search notes containing a tag, use:

```bash
notes search -t tagname
```

#### List Notes

Lists notes by modification time or filtered by tags.

```bash
notes list
```

To list notes tagged with a specific label:

```bash
notes list -t tagname
```

#### Show Note Content

Displays note contents in the terminal.

```bash
notes show mynote
```

---

### Sample Workflows

1. **Add a new note**

```bash
notes edit "project-ideas"
# Write your ideas in the opened editor, then save and exit.
```

2. **Search notes containing "meeting"**

```bash
notes search meeting
```

3. **List notes tagged as "todo"**

```bash
notes list -t todo
```

4. **View the content of a note**

```bash
notes show project-ideas
```

---

## API Reference

### Main Commands

#### `notes edit [note-name]`

- Description: Open a note in editor for creation or modification.
- Parameters:
  - `note-name` (string): The name of the note (file) to edit.
- Behavior:
  - Opens the note file in the editor specified by `$EDITOR`.
  - If no note-name is provided, may open a default note or prompt for input.

#### `notes search [pattern]`

- Description: Search notes by keyword or tag.
- Parameters:
  - `pattern` (string): The search keyword or regex pattern.
  - `-t`, `--tag` (string, optional): Filter notes by tag.
- Behavior:
  - Returns a list of notes matching the pattern or tag.
  - Supports regex for advanced search patterns.

#### `notes list`

- Description: List all notes.
- Options:
  - `-t`, `--tag` (string, optional): Filter list by tag.
  - `-r`, `--recent` (bool): Sort by recent modification.
- Behavior:
  - Lists notes with optional filtering by tags or sorted by recent activity.

#### `notes show [note-name]`

- Description: Output the content of a specified note.
- Parameters:
  - `note-name` (string): Name of the note to display.
- Behavior:
  - Prints the content of the note to the terminal.

### Configuration and Environment

- Notes directory path can be configured via environment variable `NOTES_DIR`. Default location is `~/notes`.
- Editor is selected from the `$EDITOR` environment variable.
- Tags are recognized as words prefixed with `#` in note content.

---

## License

`notes-cli` is licensed under the MIT License. See [LICENSE](https://github.com/rhysd/notes-cli/blob/master/LICENSE) in the repository for details.
