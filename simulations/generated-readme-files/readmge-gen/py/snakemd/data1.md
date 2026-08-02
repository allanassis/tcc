# SnakeMD

## Overview

SnakeMD is a command-line tool and Python library designed to convert Markdown or a subset of Markdown with embedded Python code into styled, easy-to-read HTML resumes or CVs. It emphasizes simplicity in creating personalized resumes with full Markdown syntax and Python integration, enabling dynamic content generation.

### Domain Concepts

- **Markdown Parsing:** SnakeMD processes Markdown content, including headings, lists, links, and styling.
- **Python Code Execution:** Embedded Python code within the Markdown can be executed to dynamically inject content.
- **Resume/CV Styling:** The tool applies a clean, professional style to the generated HTML for resumes.
- **Templating and Export:** Conversion from Markdown format to styled HTML output for easy distribution or web publishing.

SnakeMD models the domain of resume writing and web publishing, facilitating both static and programmatically crafted resume content with Python-augmented Markdown.

---

## Installation

Ensure Python 3.6+ is installed.

### Install via pip

```bash
pip install snakemd
```

---

## Usage and Examples

### Command Line Interface (CLI) Usage

To convert a Markdown resume into styled HTML, use:

```bash
snakemd input_resume.md -o output_resume.html
```

Where:

- `input_resume.md` is your source Markdown file with optional embedded Python.
- `-o output_resume.html` specifies the output HTML file.

### Example Markdown snippet with embedded Python code

```markdown
# John Doe

Email: {{ "john.doe@example.com" }}

## Skills

- Python
- Markdown
- Web Development

## Summary

This resume was generated on {{ import datetime; datetime.datetime.now().strftime("%Y-%m-%d") }}.
```

Using SnakeMD, the `{{ ... }}` blocks are treated as Python code and evaluated during conversion.

### Using SnakeMD as a Python Library

```python
from snakemd import SnakeMD

# Sample markdown content with embedded Python
markdown_text = """
# Jane Doe

Email: {{ "jane.doe@example.com" }}

## Projects

- SnakeMD - A Markdown to styled resume converter.

Date generated: {{ import datetime; datetime.datetime.today().strftime("%B %d, %Y") }}
"""

converter = SnakeMD()
html_output = converter.render(markdown_text)

print(html_output)
```

This produces the styled HTML resume content as a string.

---

## API Reference

### Class: `SnakeMD`

Main class providing conversion functionalities from Markdown with embedded Python to HTML.

#### Methods:

- `SnakeMD.render(markdown_text: str) -> str`
  - Converts the input Markdown text into styled HTML.
  - Executes Python code embedded within `{{ ... }}` placeholders.
  - Returns the resulting HTML string.
  - Raises exceptions on syntax errors in embedded Python or markdown processing.

- `SnakeMD.render_file(input_path: str) -> str`
  - Reads a Markdown file, processes embedded Python, and returns HTML content as string.
  - Used internally by CLI for file conversion.

### Command Line Options

- `snakemd <input_file>`: Converts the Markdown file to HTML and prints it to stdout.
- `-o, --output <output_file>`: Specifies a file to save the HTML output.
- `-h, --help`: Show help message and usage instructions.

---

## License

SnakeMD is licensed under the MIT License. See the [LICENSE](https://github.com/TheRenegadeCoder/SnakeMD/blob/main/LICENSE) file for details.
