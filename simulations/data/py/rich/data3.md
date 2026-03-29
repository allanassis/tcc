# Rich

## Overview

Rich is a Python library for rich text and beautiful formatting in the terminal. It enables developers to create visually appealing command-line interfaces by providing tools to render styled text, progress bars, tables, markdown, syntax highlighting, tracebacks, and more with color and formatting. The core domain concepts of Rich revolve around terminal styling, markup, rendering, and layout.

### Key Domain Concepts

- **Styled Text and Markup:** Rich models text with styles, colors, and decorations, represented as spans or labels within strings or objects.
- **Renderable Objects:** Abstract representations of anything that can be displayed in the terminal, including tables, panels, progress bars, and syntax trees.
- **Layouts & Console:** Management of terminal rendering space and output contexts.
- **Syntax Highlighting:** Parses source code in many languages and renders it colorfully.
- **Progress and Live Update:** Visual progress bars and real-time terminal display updates.
- **Tables and Grids:** Display complex tabular data with flexible styling.
- **Tracebacks and Logging:** Enhanced, colored tracebacks and integration with Python logging module.

Rich is widely used to improve user experience in CLI applications, debugging, reporting, and interactive sessions by exploiting modern ANSI terminal capabilities.

---

## Installation

Rich supports Python 3.6 and above. Installation is straightforward with pip.

```bash
pip install rich
```

Optionally, for Jupyter notebook integration, install with:

```bash
pip install rich[jupyter]
```

Rich is cross-platform and supports all major operating systems with compatible terminals.

---

## Usage and Examples

### Basic Console Output with Styling

```python
from rich.console import Console

console = Console()
console.print("Hello, [bold magenta]Rich[/bold magenta]!")
```

Expected output: The word "Rich" appears bold and magenta in the terminal.

### Creating and Displaying a Table

```python
from rich.console import Console
from rich.table import Table

table = Table(title="Star Wars Movies")

table.add_column("Release Year", justify="right", style="cyan", no_wrap=True)
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right", style="green")

table.add_row("1977", "Star Wars: A New Hope", "$775 million")
table.add_row("1980", "The Empire Strikes Back", "$550 million")
table.add_row("1983", "Return of the Jedi", "$475 million")

console = Console()
console.print(table)
```

This creates a styled table with columns aligned and colored appropriately.

### Syntax Highlighting Example

```python
from rich.console import Console
from rich.syntax import Syntax

code = '''
def greet(name):
    print(f"Hello, {name}")
'''

syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console = Console()
console.print(syntax)
```

Outputs the Python code snippet with syntax coloring and line numbers.

### Progress Bar Example

```python
from rich.progress import Progress
import time

progress = Progress()
task = progress.add_task("[red]Processing...", total=100)

with progress:
    for i in range(100):
        time.sleep(0.05)
        progress.update(task, advance=1)
```

Displays a progress bar that fills gradually over time.

---

## API Reference

### `rich.console.Console`

Core console class for rich text output.

- `print(*objects, sep=" ", end="\n", style=None, justify=None, overflow=None, no_wrap=False, emoji=True, markup=True)`

  Prints objects to the console with rich styling and markup support.

- `input(prompt)`

  Outputs a prompt and reads input from the user.

- `rule(title=None, characters=None, style=None)`

  Prints a styled horizontal rule with an optional title.

- `clear()`

  Clears the console screen.

---

### `rich.table.Table`

Create styled tables for tabular data.

- `Table(title=None, show_header=True, header_style=None, show_footer=False, footer_style=None, caption=None, caption_style=None, padding=(0,1), expand=False)`

  Constructor with optional styling and header/footer display.

- `add_column(header, style=None, justify=None, no_wrap=False, ratio=None, min_width=0, max_width=None)`

  Adds a column to the table.

- `add_row(*cells, style=None, end_section=False)`

  Adds a row of cells to the table.

---

### `rich.syntax.Syntax`

Render syntax-highlighted source code.

- `Syntax(code, lexer_name, *, theme="default", line_numbers=False, word_wrap=False, indent_guides=False, highlight_lines=None, code_width=None, background_color=None)`

  Constructor parameters allow fine control over highlighting, formatting, and display.

---

### `rich.progress.Progress`

Display progress bars.

- `add_task(description, total=None, completed=0, visible=True, start=True)`

  Adds a new progress task.

- `update(task_id, completed=None, advance=None, description=None)`

  Updates task progress.

- `start_task(task_id)`

  Starts a paused task.

- `stop_task(task_id)`

  Stops a running task.

---

### `rich.traceback.Traceback`

Render pretty tracebacks with color and syntax highlighting.

- `Traceback.from_exception(exception)`

  Creates a Traceback object from an exception instance.

- `console.print(traceback)`

  Prints the traceback with rich formatting.

---

### `rich.logging.RichHandler`

Logging handler that renders logs in the console with rich formatting.

- Usage:

```python
import logging
from rich.logging import RichHandler

logging.basicConfig(level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler()])
log = logging.getLogger("rich")
log.info("Hello, Rich logging!")
```

---

## License

Rich is distributed under the [MIT License](https://github.com/Textualize/rich/blob/master/LICENSE).
