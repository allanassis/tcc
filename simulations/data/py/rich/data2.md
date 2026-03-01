# Rich

## Overview

Rich is a Python library for rich text and beautiful formatting in the terminal. It provides tools to render styled text, tables, progress bars, syntax highlighting, markdown, tracebacks, and more, allowing developers to create visually appealing and highly readable command-line interfaces (CLI).

### Domain Concepts

- **Styled Text and Colors:** Rich models terminal text styling using colors, styles (bold, italic, underline), and emoji support.
- **Layouts and Panels:** Organizes output into structured layouts with panels, columns, and grids.
- **Tables:** Constructs tables with flexible options for alignment, styling, and borders.
- **Syntax Highlighting:** Detects and highlights source code in multiple languages.
- **Progress Bars:** Intelligent progress bars with multiple tasks and spinners.
- **Console Rendering:** Output abstraction to render these elements to the terminal with appropriate escape codes.
- **Live Updating:** Dynamic output updating for animations, real-time data, and logs.
- **Logging:** Integration to render formatted logs directly to the terminal.
- **Tracebacks and Exceptions:** Render rich tracebacks enriched with syntax highlighting and better readability.

Rich is designed to work as a drop-in replacement for standard Python terminal output using simple API calls while enhancing user experience with eye-catching console applications.

---

## Installation

Rich requires Python 3.6 or newer.

### Install via pip

```bash
pip install rich
```

### Install the latest development version

```bash
pip install git+https://github.com/Textualize/rich.git
```

Rich is cross-platform supporting Linux, macOS, and Windows terminals (including Windows Terminal, PowerShell, and cmd).

---

## Usage and Examples

Rich can be used by importing the `Console` class and other components.

### Basic Console Output

```python
from rich.console import Console

console = Console()
console.print("Hello, [bold magenta]Rich[/bold magenta]!")
```

**Output:**
Renders "Hello, Rich!" where "Rich" is bold and magenta colored.

---

### Tables

```python
from rich.console import Console
from rich.table import Table

console = Console()
table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("1977", "A New Hope", "$775,398,007")
table.add_row("1980", "The Empire Strikes Back", "$547,969,004")
table.add_row("1983", "Return of the Jedi", "$475,106,177")

console.print(table)
```

Renders a colorful styled table with headers and data aligned and colored.

---

### Progress Bars

```python
from rich.progress import track
import time

for step in track(range(100), description="Processing..."):
    time.sleep(0.05)
```

Shows an updating progress bar with a description while iterating.

---

### Syntax Highlighting

```python
from rich.console import Console
from rich.syntax import Syntax

code = '''def greet(name):
    print(f"Hello, {name}!")'''

console = Console()
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

Displays Python code with syntax highlighting and optional line numbers.

---

### Logging

```python
import logging
from rich.logging import RichHandler

logging.basicConfig(
    level="NOTSET",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler()]
)

log = logging.getLogger("rich")
log.info("This is an info log with [bold green]Rich[/bold green] style!")
```

Enables richly formatted logging output in the terminal.

---

## API Reference

### `rich.console.Console`

Primary class to write styled and formatted output to the terminal.

- `print(*objects, sep=' ', end='\n', style=None, justify=None)`: Print styled text, objects, or markup with optional style and justification.
- `rule(text=None, style=None, align="center")`: Draw a horizontal rule line optionally with centered text.
- `clear()`: Clears the terminal.
- `status(text, spinner='dots')`: Context manager to display a status spinner with a message.
- `input(prompt)`: Get input from the user with formatted prompt.

### `rich.table.Table`

Creates tables with columns and rows.

- `add_column(header, style=None, justify="left", no_wrap=False)`: Adds a column with styling.
- `add_row(*cells, style=None, end_section=False)`: Adds a row of cells with optional style.

### `rich.progress.track(iterable, description=None, **kwargs)`

Helper function to iterate with a progress bar on the terminal.

### `rich.syntax.Syntax(code, lexer_name, **options)`

Render syntax-highlighted code.

- `code`: Source code string.
- `lexer_name`: Language name (e.g. "python", "json").
- Options: `theme`, `line_numbers` (bool), etc.

### `rich.logging.RichHandler`

Logging handler to produce rich-formatted log output.

---

## Contributing

Contributions to Rich are welcome! You can submit bug reports, suggest features, or contribute code.

### How to contribute

1. Fork the repository: https://github.com/Textualize/rich
2. Create a new branch for your feature or bug fix.
3. Write clear and concise code following existing style.
4. Add tests for your changes.
5. Submit a pull request describing your changes.

For detailed guidelines, see the [CONTRIBUTING.md](https://github.com/Textualize/rich/blob/master/CONTRIBUTING.md) file.

---

## License

Rich is licensed under the [MIT License](https://github.com/Textualize/rich/blob/master/LICENSE).

---

## Contact

- GitHub Repository: [https://github.com/Textualize/rich](https://github.com/Textualize/rich)
- Issues and feature requests: Use GitHub Issues page
- Discussions and help: https://github.com/Textualize/rich/discussions
