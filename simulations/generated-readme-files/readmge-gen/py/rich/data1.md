# Rich

## Overview

Rich is a Python library for rich text and beautiful formatting in the terminal. It enables developers to enhance the command-line interface (CLI) output with colors, styles, tables, progress bars, syntax highlighting, markdown rendering, tracebacks, and more. The core domain concepts modeled by Rich include terminal styling, text rendering, layout management, and live updates of console output, which facilitate creating visually appealing and user-friendly terminal applications.

### Domain Concepts

- **Console**: The main entry point for printing styled text and rich content.
- **Text Styling**: Attributes like color, bold, italic, underline, and more to style terminal text.
- **Markup & ANSI Escape Codes**: Parsing and rendering of markup for styles and colors, and working with ANSI escape sequences.
- **Syntax Highlighting**: Highlighting source code with language-specific lexers.
- **Tables & Layouts**: Structured presentation of tabular data and flexible layout management.
- **Progress Bars**: Visual display of task progress.
- **Live Updates**: Dynamically updating terminal output without flickering.
- **Tracebacks**: Enhanced error tracebacks with syntax highlighting and context.
- **Panels, Boxes, and Trees**: Visual containers and hierarchical data representations.

Rich closely models terminal output capabilities and the concept of stylizing and layering information in text interfaces.

---

## Installation

Rich is compatible with Python 3.6 and above.

You can install it using pip:

```bash
pip install rich
```

To upgrade to the latest version:

```bash
pip install --upgrade rich
```

---

## Usage and Examples

### Printing Rich Text

```python
from rich.console import Console

console = Console()
console.print("[bold magenta]Hello[/bold magenta] [green]World[/green]!", justify="center")
```

Output: Styled text "Hello" in bold magenta, followed by "World" in green, centered.

### Using Markup to Style Text

```python
console.print("This is [red]red[/red] and this is [underline]underlined[/underline].")
```

### Table Example

```python
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Released", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("1977", "A New Hope", "$775,398,007")
table.add_row("1980", "The Empire Strikes Back", "$547,969,004")
table.add_row("1983", "Return of the Jedi", "$475,106,177")

console.print(table)
```

### Progress Bar Example

```python
from rich.progress import track
import time

for step in track(range(100), description="Processing..."):
    time.sleep(0.02)
```

### Syntax Highlighting Example

```python
from rich.syntax import Syntax

code = '''def hello_world():
    print("Hello, World!")'''

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

### Live Updating Example

```python
from rich.live import Live
from rich.table import Table
import time

table = Table()

table.add_column("Row ID")
table.add_column("Description")

with Live(table, refresh_per_second=4):
    for i in range(10):
        table.add_row(str(i), f"description {i}")
        time.sleep(0.4)
```

---

## API Reference

### rich.console.Console

The main interface to print styled and rich content to the terminal.

- `Console(file=None, force_terminal=False, color_system=None, width=None, ... )`

  Creates a Console instance.

- `print(*objects, sep=' ', end='\n', style=None, justify=None, markup=False, emoji=True, highlight=False)`

  Prints objects with rich formatting.

- `clear()`

  Clears the terminal screen.

- `status(text, spinner='dots')`

  Context manager to display a status spinner.

### rich.text.Text

A text object that supports complex styling and formatting.

- `Text(text, style=None, justify=None, overflow=None, no_wrap=False, ...)`

- `append(text, style=None, ...)`

- `stylize(style, start=None, end=None)`

### rich.table.Table

Constructs a table with columns and rows, supporting styles and alignment.

- `add_column(header, style=None, justify=None, no_wrap=False)`

- `add_row(*cells, style=None)`

- `show_header(show=True)`

### rich.progress.Progress

Progress bar manager to display progress for tasks.

- `add_task(description, total=None, ...)`

- `update(task_id, advance=1)`

- `start()`, `stop()`

### rich.syntax.Syntax

Syntax highlighter for source code, supporting multiple languages.

- `Syntax(code, lexer_name, theme=None, line_numbers=False)`

### rich.traceback.Traceback

Enhanced traceback display with syntax highlighting.

- `Traceback.from_exception(exc_type, exc_value, traceback)`

### rich.prompt.Prompt

Prompt user for input with styles and validation.

- `Prompt.ask(question, choices=None, default=None, password=False)`

---

## License

Rich is distributed under the MIT License. See the [LICENSE](https://github.com/Textualize/rich/blob/master/LICENSE) file for detailed license information.
