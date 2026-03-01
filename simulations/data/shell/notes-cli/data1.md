# notes-cli

## Overview

`notes-cli` is a command-line tool designed to help users take, manage, and search notes efficiently from their terminal. It simplifies note-taking by allowing notes to be stored in plain text files and supports quick search and retrieval using fuzzy search features. The tool focuses on lightweight, keyboard-driven workflows catered toward developers, writers, and users who prefer terminal-based note management.

### Domain Concepts

- **Notes and Note Files:** `notes-cli` treats individual notes as text files stored in a specified directory, each representing a separate note.
- **Tagging and Searching:** Users can tag notes via hashtags in the content and perform content-based or tag-based searches.
- **TUI (Text User Interface):** It provides a terminal-based interactive interface for browsing, creating, editing, and searching notes.
- **Fuzzy Search:** Implements fuzzy search algorithms to quickly filter notes matching search queries.
- **Integration with Editors:** Supports launching notes in external editors configured by the user.

The tool models the domain concepts of note-taking, text search, and terminal interactions to streamline personal knowledge management in a developer-friendly environment.

---

## Installation

`notes-cli` can be installed on Unix-like systems and requires Go and typical command line tools.

### Using Go

If you have Go installed, you can install `notes-cli` using:

```bash
go install github.com/rhysd/notes-cli@latest
```

Make sure your Go bin directory is in your PATH to run the command directly.

### Using Prebuilt Binaries

Check the [GitHub Releases](https://github.com/rhysd/notes-cli/releases) page for precompiled binaries for various OS and architectures. Download the appropriate binary for your platform, make it executable, and place it in your PATH.

### Dependencies

- A modern Unix-like environment (Linux, macOS).
- Optional: A configured text editor like `vim`, `nano`, or others for note editing.

---

## Usage and Examples

### Basic Usage

Initialize your notes directory (environment variable or config):

```bash
export NOTES_DIR="$HOME/notes"
mkdir -p $NOTES_DIR
```

Start `notes-cli`:

```bash
notes
```

This opens an interactive terminal UI listing your notes.

### Creating a New Note

In the interface, press `n` to create a new note. Enter the title, and the note file will be created.

Alternatively, create notes by adding files to the `NOTES_DIR`.

### Searching Notes

Type `/` followed by your search query to filter notes using fuzzy search matching titles and contents.

### Editing a Note

Select a note and press `e` to open it in the configured editor.

### Command-line Options

```bash
notes -h
```

Shows help and available flags:

- `-dir string` : Specify notes directory (default uses `NOTES_DIR` env var).
- `-editor string` : Specify what editor to open notes in (default depends on `$EDITOR` env).
- `-version` : Show version information.

### Example: Run notes in custom directory with Vim editor

```bash
notes -dir $HOME/my_notes -editor vim
```

---

## API Reference

Since `notes-cli` is a CLI application, it exposes a limited programmatic API primarily through command-line flags and terminal keyboard shortcuts.

### CLI Flags

- `-dir string`

  Notes directory location. Defaults to environment variable `NOTES_DIR` or current directory.

- `-editor string`

  External editor command to open notes (e.g., `vim`, `nano`, `code`).

- `-version`

  Prints version information and exits.

### Keyboard Shortcuts (when running interactively)

- `n`: Create a new note.
- `/`: Start incremental search for filtering notes.
- Arrow keys: Navigate note list.
- `e`: Edit selected note.
- `d`: Delete selected note.
- `q`: Quit the program.

---

## Contributing

Contributions to `notes-cli` are welcome! To contribute:

1. Fork the repository on GitHub.
2. Create a feature branch for your changes: `git checkout -b feature-name`.
3. Make changes with tests or documentation updates as needed.
4. Submit a pull request with a description of your changes.

Please check existing issues and the contribution guidelines on the repository. Engage in discussions to propose new features or report bugs.

---

## License

`notes-cli` is licensed under the MIT License. See the LICENSE file in the repository for details.

---

## Contact

- **Repository:** https://github.com/rhysd/notes-cli
- **Issues:** Use GitHub Issues page for bug reports and feature requests.
- **Author:** Rhysd
