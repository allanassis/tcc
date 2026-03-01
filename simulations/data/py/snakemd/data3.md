# SnakeMD

## Overview

SnakeMD is a Markdown editor designed for the terminal, bringing a powerful and user-friendly Markdown editing experience to command-line interfaces. It focuses on providing live preview, smooth navigation, and full Markdown support, enabling users to create and edit Markdown files efficiently without leaving the terminal environment.

### Domain Concepts

- **Markdown Editing:** SnakeMD models the domain concepts of Markdown syntax, including headings, lists, links, code blocks, and formatting styles.
- **Terminal-based UI:** It embraces terminal-based text editing paradigms with concepts like screens, buffers, and keybindings adapted for Markdown.
- **Live Preview:** The tool shows a real-time rendered version of the Markdown content alongside or integrated with the editor.
- **Navigation & Interaction:** Uses keyboard shortcuts and commands for editing, previewing, and managing Markdown documents entirely within the terminal.

SnakeMD aims to streamline Markdown writing workflows for developers and writers who prefer terminal tools yet want rich Markdown support.

---

## Installation

You can install SnakeMD on multiple platforms. It requires Rust and Cargo, the Rust package manager.

### Prerequisites

- Rust and Cargo installed. See the official Rust installation guide: https://rustup.rs/

### Install via Cargo

```bash
cargo install snakemd
```

### Download pre-built binaries

Visit the GitHub releases page and download the binary for your platform:  
https://github.com/TheRenegadeCoder/SnakeMD/releases

### Build from source

Clone the repo and build manually:

```bash
git clone https://github.com/TheRenegadeCoder/SnakeMD.git
cd SnakeMD
cargo build --release
```

The executable will be in the `target/release` directory.

---

## Usage and Examples

### Basic usage

To open or create a Markdown file:

```bash
snakemd file.md
```

This opens `file.md` in the SnakeMD editor. If the file does not exist, it creates a new one.

### Navigation and editing

- Use arrow keys, PageUp/PageDown to navigate.
- Use standard Markdown syntax to write headings, lists, links, etc.
- Keyboard shortcuts provide quick access to formatting, help, and preview.

### Live preview mode

Toggle the live Markdown preview with:

```
Ctrl + P
```

This renders the current Markdown content as formatted text in the terminal alongside the editor.

### Common keybindings

| Shortcut | Action              |
| -------- | ------------------- |
| Ctrl + S | Save current file   |
| Ctrl + Q | Quit the editor     |
| Ctrl + P | Toggle live preview |
| Ctrl + H | Show help           |

---

## API Reference

As a terminal application written in Rust, SnakeMD's main user-facing APIs are its command-line interface and keyboard shortcuts. For developers interested in extending or understanding the internal API, the core modules and their execution facts include:

### Command-line Interface (CLI)

- `snakemd <filepath>`

  Opens the specified Markdown file or creates a new one if it doesn't exist.

- Flags:
  - `--help` or `-h`: Displays help information.
  - `--version` or `-v`: Shows the current version of SnakeMD.

### Core Modules (for developers)

- **Editor Module**

  Handles input capturing, text insertion, deletion, cursor movement, and buffer management.

- **Renderer Module**

  Parses Markdown source to terminal-rendered formatted text for live preview.

- **UI Module**

  Manages terminal UI layout, including editor pane and preview pane, handles keyboard events and screen refresh.

- **File Module**

  Responsible for filesystem interactions: reading and writing Markdown files.

### Execution Facts

- Opening a file loads its content into the editor buffer.
- Key presses trigger event handlers that modify the buffer or the UI state.
- The live preview updates upon buffer changes and renders Markdown to terminal output.
- Saving writes the buffer contents back to the file atomically.
- Quitting exits gracefully after prompting to save unsaved changes.

---

## Contributing

Contributions to SnakeMD are welcome! Whether you want to fix bugs, improve documentation, or add new features:

1. Fork the repository on GitHub.
2. Create a feature branch (`git checkout -b feature-name`).
3. Make your changes with clear commit messages.
4. Test your changes to ensure no regressions.
5. Submit a pull request for review.

Please adhere to Rust coding conventions and existing project style guidelines.

---

## License

SnakeMD is distributed under the MIT License. See the [LICENSE](https://github.com/TheRenegadeCoder/SnakeMD/blob/main/LICENSE) file for details.

---

## Contact

- **GitHub Repository:** [https://github.com/TheRenegadeCoder/SnakeMD](https://github.com/TheRenegadeCoder/SnakeMD)
- For issues and feature requests, use the [GitHub Issues](https://github.com/TheRenegadeCoder/SnakeMD/issues) page.
- Community discussions and contributions are welcome via GitHub pull requests.

---

## Example Session

Open a file for editing:

```bash
snakemd notes.md
```

Write Markdown content, toggle live preview with `Ctrl + P`, save with `Ctrl + S`, and quit with `Ctrl + Q`.

Enjoy seamless terminal-based Markdown editing powered by SnakeMD!
