# SnakeMD

## Overview

SnakeMD is a command-line tool designed to convert Markdown files with code blocks into syntax-highlighted and visually enhanced HTML documents. It specializes in taking Markdown content and adding colorized code snippets by using the Python Pygments library, making it easier to share, present, or publish Markdown content with beautifully formatted code.

### Domain Concepts

- **Markdown:** A lightweight markup language with plain-text formatting syntax, widely used for documentation.
- **Code Blocks:** Sections of code encapsulated within Markdown notation for programming language snippets.
- **Syntax Highlighting:** The process of coloring key syntactical elements in source code to improve readability.
- **HTML Generation:** Converting Markdown and highlighted code into web-ready HTML outputs.
- **CLI (Command-Line Interface):** Users interact with the tool via terminal commands.

SnakeMD thus models the domain concepts of Markdown formatting and syntax highlighting, bridging them to web presentation.

---

## Installation

### Prerequisites

- Python (3.6 or higher)
- Pip (Python package installer)

### Install from PyPI

```bash
pip install snakemd
```

### Install from source

```bash
git clone https://github.com/TheRenegadeCoder/SnakeMD.git
cd SnakeMD
pip install .
```

---

## Usage and Examples

### Basic CLI Usage

Convert a Markdown file to highlighted HTML:

```bash
snakemd input.md output.html
```

This command reads `input.md`, processes its code blocks with syntax highlighting, and writes the HTML result to `output.html`.

### Options

- `-t`, `--theme`: Specify a Pygments style theme for code highlighting (e.g., `monokai`, `friendly`, `default`). Example:

```bash
snakemd input.md output.html -t monokai
```

### Usage as a Python module

```python
from snakemd import SnakeMD

converter = SnakeMD(theme='monokai')
html_output = converter.convert('path/to/input.md')

with open('output.html', 'w', encoding='utf-8') as f:
    f.write(html_output)
```

---

## API Reference

### Class: `SnakeMD`

Core class responsible for converting Markdown with code blocks into syntax-highlighted HTML.

#### Constructor:

```python
SnakeMD(theme: str = 'default')
```

- `theme`: (Optional) The Pygments style theme used for syntax highlighting. Defaults to `'default'`.

#### Methods:

- `convert(file_path: str) -> str`

  Reads a Markdown file from the given path, processes it, and returns an HTML string with syntax-highlighted code.
  - `file_path`: Path to the source Markdown file.
  - Returns: HTML string with highlighted code blocks included.

- `convert_markdown_text(md_text: str) -> str`

  Converts Markdown text provided as a string directly into highlighted HTML.
  - `md_text`: Markdown content as a string.
  - Returns: HTML string.

---

## Contributing

Contributions to SnakeMD are highly welcome! To contribute:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix (`git checkout -b feature-name`).
3. Add tests and ensure existing tests pass.
4. Submit a Pull Request with a detailed description of the changes.

Please follow PEP8 style guidelines for Python code and document your changes properly.

---

## License

SnakeMD is distributed under the MIT License. See the [LICENSE](https://github.com/TheRenegadeCoder/SnakeMD/blob/master/LICENSE) file for details.

---

## Contact

- **Repository:** [https://github.com/TheRenegadeCoder/SnakeMD](https://github.com/TheRenegadeCoder/SnakeMD)
- **Issues:** Use GitHub Issues to report bugs or suggest features.

For additional help, visit the project page or open an issue.
