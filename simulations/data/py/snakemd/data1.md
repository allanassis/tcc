# SnakeMD

## Overview

SnakeMD is a command-line tool that converts Markdown files into well-formatted terminal output with color and style, enhancing the readability of Markdown documents directly in the terminal. It is designed to bring the beauty and structure of Markdown to terminal users without needing to view the files in a browser or editor supporting Markdown syntax.

### Domain Concepts

- **Markdown Rendering:** SnakeMD interprets Markdown syntax such as headings, lists, code blocks, links, emphasis, and tables to produce styled terminal output.
- **Terminal Styling:** Utilizes terminal color and text styles (bold, italic, underline) and Unicode symbols to enhance Markdown visualization.
- **Command Line Interface:** Provides a terminal command that accepts Markdown files as input and outputs transformed content to the terminal.
- **Parsing and Formatting:** Internally parses Markdown content and maps it to styled terminal sequences for display.

By understanding these concepts, users can effectively convert and preview Markdown content for documentation, notes, READMEs, or other purposes directly in a terminal environment.

---

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installing via pip

```bash
pip install snakemd
```

This installs the `snakemd` CLI tool globally.

### Alternative: Clone and Install Manually

```bash
git clone https://github.com/TheRenegadeCoder/SnakeMD.git
cd SnakeMD
pip install .
```

---

## Usage and Examples

### Basic Usage

Render a Markdown file to the terminal:

```bash
snakemd README.md
```

This command parses the `README.md` file and outputs the styled content in the terminal.

### Using SnakeMD in Python Code

You can also use SnakeMD programmatically via its API to convert Markdown strings to styled terminal text.

Example:

````python
from snakemd import snakemd

md_content = """
# Hello World

This is a *sample* **Markdown** document.

- Item 1
- Item 2

`inline code`

```python
def greet():
    print("Hello, SnakeMD!")
````

"""

styled_output = snakemd.snakemd_to_ansi(md_content)
print(styled_output)

````

This will print the Markdown content with colors and styles appropriate for terminal display.

### Options

- `-c` or `--color`: Enable or disable color output.
- `-t` or `--theme`: Choose a color theme if available.
- `-v` or `--version`: Show version information.
- `-h` or `--help`: Show help message.

Example with options:

```bash
snakemd -c False example.md
````

Disables color output.

---

## API Reference

### `snakemd.snakemd_to_ansi(md_text: str) -> str`

Converts Markdown text to an ANSI-colored string suitable for terminal output.

- **Parameters:**
  - `md_text` (str): The Markdown formatted string.
- **Returns:**
  - `str`: A string with ANSI escape codes for terminal styling.

### `snakemd.snakemd_cli()`

The main entry point for the command-line interface. Processes command-line arguments and outputs styled Markdown.

### Command-Line Interface

- Accepts one or more Markdown file paths or stdin input.
- Parses Markdown content.
- Writes styled terminal output to stdout.

---

## Contributing

Contributions to SnakeMD are welcome! You can help by:

- Reporting issues or bugs on the GitHub issue tracker.
- Submitting pull requests with bug fixes, new features, or improvements.
- Improving documentation or adding examples.
- Suggesting or implementing new themes for terminal rendering.

### How to contribute

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-or-bugfix`).
3. Make your changes and commit with clear messages.
4. Push the branch and submit a pull request on GitHub.

Please ensure tests pass and code style aligns with the repository before submitting.

---

## License

SnakeMD is licensed under the MIT License. See the [LICENSE](https://github.com/TheRenegadeCoder/SnakeMD/blob/master/LICENSE) file for details.

---

## Contact

- GitHub Repository: [https://github.com/TheRenegadeCoder/SnakeMD](https://github.com/TheRenegadeCoder/SnakeMD)
- Issues and Feature Requests: Use GitHub issues at the repository page.
- Maintainer: The Renegade Coder (GitHub community)

For questions or support, please open an issue on GitHub.

```

```
