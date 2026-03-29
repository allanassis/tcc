# Rich

## Overview

Rich is a Python library for rich text and beautiful formatting in the terminal. It enables developers to create visually appealing terminal applications by providing advanced capabilities for styling text with colors, gradients, and styles, as well as rendering complex layouts, tables, progress bars, markdown, syntax highlighting of source code, and more.

The main domain concepts of Rich include:

- **Styled Text:** Applying colors, bold, italic, underline, and other styles to terminal text using markup or programmatic APIs.
- **Console Rendering:** Using a Console object to print richly formatted content and control terminal output.
- **Layouts:** Managing sophisticated terminal layouts to display multiple panels or columns.
- **Components:** Rich provides renderable elements such as Panels, Tables, Trees, Progress Bars, and Syntax Highlighting.
- **Live Updates:** Dynamically updating terminal output, such as progress bars and live data refresh.
- **High-Level Abstractions:** Supporting Markdown rendering, tracebacks with color and formatting, and interactive prompts.

Rich focuses on making it easy to build beautiful and production-ready CLI applications, improving readability and providing a more engaging user experience in the terminal environment.

---

## Installation

To install Rich, ensure you have Python 3.6 or above, then install via pip:

```bash
pip install rich
```

You can also install the latest development version from GitHub for cutting-edge features:

```bash
pip install git+https://github.com/Textualize/rich.git
```

Rich is compatible with Linux, macOS, and Windows terminals that support ANSI escape codes.

---

## Usage and Examples

### Basic Console Output with Styling

```python
from rich.console import Console

console = Console()

console.print("Hello, [bold magenta]Rich[/bold magenta]!", style="underline on yellow")
```

Expected output: The word "Rich" is printed in bold magenta and the entire string is underlined on a yellow background.

---

### Printing a Table

```python
from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="User Information")

table.add_column("ID", justify="right", style="cyan", no_wrap=True)
table.add_column("Name", style="magenta")
table.add_column("Role", style="green")

table.add_row("1", "Alice", "Developer")
table.add_row("2", "Bob", "Manager")
table.add_row("3", "Charlie", "Designer")

console.print(table)
```

Expected: A formatted table with colored columns and a title displayed in the terminal.

---

### Syntax Highlighting for Code

```python
from rich.console import Console
from rich.syntax import Syntax

console = Console()

code = '''def greet(name):
    print(f"Hello, {name}!")'''

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

Expected: Python code snippet printed with syntax highlighting and line numbers.

---

### Progress Bar Example

```python
from rich.progress import track
import time

for step in track(range(100), description="Processing..."):
    time.sleep(0.05)
```

Expected: A progress bar with a description "Processing..." that updates in place.

---

### Live Updating Panel

```python
from rich.live import Live
from rich.panel import Panel
from time import sleep
import random

with Live(Panel("Starting..."), refresh_per_second=4) as live:
    for _ in range(10):
        live.update(Panel(f"Random value: {random.randint(1, 100)}"))
        sleep(0.5)
```

Expected: A panel in the terminal that updates dynamically with new random values.

---

## API Reference

### `Console`

The central object for writing richly formatted text and components to the terminal.

- **Methods:**
  - `.print(*objects, sep=' ', end='\n', style=None, justify=None, emoji=True, markup=True, highlight=False, ... )`: Prints objects with rich formatting support.
  - `.input(prompt, password=False)`: Accepts user input with optional password masking.
  - `.clear()`: Clears the terminal screen.
  - `.rule(title=None, style=None)`: Prints a horizontal rule separator.

---

### `Table`

Creates and displays tables with customizable columns.

- **Constructor parameters:**
  - `title` (str): Optional title for the table.
  - `show_header` (bool): Display header row (default True).
  - `header_style` (str): Style for header.
  - `show_lines` (bool): Display lines between rows.
  - `row_styles` (List[str]): Styles to alternate row colors.

- **Key methods:**
  - `.add_column(header, *, style=None, justify=None, ratio=None, no_wrap=False)`: Adds a column.
  - `.add_row(*cells, style=None)`: Adds a row of cells.

---

### `Syntax`

For syntax highlighting of source code.

- **Constructor parameters:**
  - `code` (str): The source code string.
  - `language` (str): Programming language name, e.g., "python", "json".
  - `theme` (str): Color theme, e.g., "monokai", "default".
  - `line_numbers` (bool): Show line numbers.

---

### `Progress`

A progress bar runner and manager.

- **Usage:**
  - Use `track` helper for simple loops: `for item in track(iterable, description="..."):`
  - Or create a `Progress` instance for advanced features and multiple tasks.

---

### `Panel`

A bordered box to highlight content.

- **Constructor parameters:**
  - `renderable`: Content to display inside.
  - `title` (str): Optional panel title.
  - `subtitle` (str): Optional subtitle.
  - `style` (str): Border and text styles.

---

### `Live`

Allows live updating of rendered content in the terminal.

- **Context manager usage:** `with Live(renderable, refresh_per_second=4):`
- Supports `.update(new_renderable)` to change displayed content.

---

### Additional Noteworthy Modules

- `rich.markdown` – Render GitHub-flavored Markdown to the terminal.
- `rich.tree` – Render hierarchical tree structures.
- `rich.traceback` – Enhanced tracebacks with color and formatting.
- `rich.theme` – Define and apply custom color themes.
- `rich.columns` – Arrange renderables in columns for layout.

---

## License

Rich is licensed under the [MIT License](https://github.com/Textualize/rich/blob/master/LICENSE).
