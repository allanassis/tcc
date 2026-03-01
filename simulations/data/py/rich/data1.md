# Rich

## Overview

Rich is a Python library for rich text and beautiful formatting in the terminal. It provides advanced rendering capabilities for styled text, progress bars, tables, markdown, syntax highlighting, and more. The library focuses on making terminal output visually compelling and readable with a minimal and simple API.

### Domain Concepts

- **Rich Text Rendering:** Using styles, colors, and text formatting to enhance terminal output.
- **Console:** Represents the terminal or output stream with capabilities to render rich content.
- **Markup and Markdown:** Support for lightweight markup syntax and full markdown rendering.
- **Layouts and Tables:** Organize content into panels, columns, trees, and grids.
- **Syntax Highlighting:** Highlight source code and other structured text formats with multiple languages support.
- **Progress Bars:** Display progress with advanced spinners and bar styles.
- **Logging Integration:** Enhanced log output with colored and styled entries.
- **Live Updating:** Dynamic refresh of console output for real-time data display.

Rich is designed to work across all major platforms and supports Python 3.6 and above.

---

## Installation

### Using pip

```bash
pip install rich
```

### Optional dependencies for enhanced features

- `pygments` for syntax highlighting.
- `colorama` on Windows for better color support (often installed automatically).

---

## Usage and Examples

### Simple Console Output with Styles

```python
from rich.console import Console
console = Console()

console.print("Hello, [bold magenta]Rich[/bold magenta]!")
```

Output: The word "Rich" appears in bold magenta color in the terminal.

---

### Rendering a Table

```python
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Fruit Prices")

table.add_column("Fruit", style="cyan")
table.add_column("Price", justify="right", style="green")

table.add_row("Apple", "$1.20")
table.add_row("Banana", "$0.50")
table.add_row("Cherry", "$2.00")

console.print(table)
```

---

### Syntax Highlighting Example

```python
from rich.console import Console
from rich.syntax import Syntax

console = Console()
code = '''
def hello():
    print("Hello, Rich!")
'''

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

---

### Progress Bar Example

```python
from rich.progress import Progress
import time

with Progress() as progress:
    task = progress.add_task("[cyan]Processing...", total=100)
    for _ in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1)
```

---

## API Reference

### `Console` class

- **Purpose:** Central class for rich text output.
- **Key methods:**
  - `print(*objects, **kwargs)`: Print styled or rich content.
  - `log(message, **kwargs)`: Print a log message with timestamp and style.
  - `input(prompt)`: Prompt user input with styling.
- **Parameters:** `file` (optional) to output to a file-like object other than stdout.

---

### `Table` class

- Used to create and render tables.
- **Key methods:**
  - `add_column(header, style=None, justify="left")`: Add a table column.
  - `add_row(*cells)`: Add a row of cells.
- Supports styled headers, rows, and columns.

---

### `Progress` class

- Displays progress bars and spinners.
- **Key methods:**
  - `add_task(description, total=None)`: Start a new task.
  - `update(task_id, advance=None, completed=None)`: Update task progress.
- Supports multiple concurrent tasks and custom spinner styles.

---

### `Syntax` class

- Renders syntax-highlighted code blocks.
- **Constructor:**
  - `Syntax(code, lexer_name, *, theme="default", line_numbers=False, highlight_lines=None)`
- Supports many programming languages via Pygments.

---

### Key Modules and Features

- `rich.text`: For styled text objects.
- `rich.markdown`: Markdown parser and renderer.
- `rich.panel`: Display bordered panels with optional titles.
- `rich.tree`: Render hierarchical tree structures.
- `rich.live`: For real-time updating displays.
- `rich.console`: Core system for rendering.
- `rich.style`: Defines text styles and colors.
- `rich.logging`: Integrates rich formatting into Python’s logging module.

---

## Contributing

Rich welcomes contributions from the community!

### Contribution Guidelines

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Ensure code is formatted using `black` and passes all tests.
4. Write tests for new features and fixes.
5. Submit a pull request with clear explanations.

Refer to the [CONTRIBUTING.md](https://github.com/Textualize/rich/blob/master/CONTRIBUTING.md) for detailed guidelines.

---

## License

Rich is licensed under the [MIT License](https://github.com/Textualize/rich/blob/master/LICENSE).

---

## Contact

- **Project repository:** [https://github.com/Textualize/rich](https://github.com/Textualize/rich)
- **Documentation:** [https://rich.readthedocs.io/](https://rich.readthedocs.io/)
- **Author:** Will McGugan (Twitter: [@willmcgugan](https://twitter.com/willmcgugan))

For support and discussions, check issues on GitHub or join the community on Discord.
