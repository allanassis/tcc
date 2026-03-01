# Rich

## Overview

Rich is a Python library for rich text and beautiful formatting in the terminal. It enables developers to render styled text, tables, progress bars, tracebacks, syntax highlighted code, markdown, and more, directly in consoles and terminal applications. Rich leverages ANSI escape sequences to provide color, style, and sophisticated layouts that greatly enhance the user interface of CLI tools, making outputs more readable and engaging.

### Domain Concepts

- **Styled Text:** Colorful text with styles such as bold, italic, underline, and strike-through.
- **Tables:** Structured presentation of tabular data with customizable borders, padding, and alignment.
- **Markdown Rendering:** Convert markdown syntax into styled terminal output.
- **Syntax Highlighting:** Highlight source code in multiple programming languages.
- **Progress Bars:** Visual indicators of long-running tasks with customizable styles and columns.
- **Tracebacks:** Enhanced tracebacks with syntax highlighted code frames and context.
- **Panels and Layouts:** Containers to organize content visually.
- **Live Updates:** Dynamic rendering to update terminal output in place.
- **Trees:** Hierarchical data visualizations with expandable nodes.

Rich abstracts complex terminal capabilities with a clean and expressive API, drastically improving the look and feel of Python CLI applications.

---

## Installation

To install Rich, ensure you have Python 3.6 or newer, then run:

```bash
pip install rich
```

For the latest development version, you can install directly from the GitHub repository:

```bash
pip install git+https://github.com/Textualize/rich.git
```

Rich supports major operating systems including Linux, macOS, and Windows with modern terminal emulators.

---

## Usage and Examples

Below are common usage patterns demonstrating Rich's capabilities.

### Styling and Printing Text

```python
from rich.console import Console

console = Console()

console.print("Hello", style="bold red")
console.print("Important:", style="bold underline green")
```

Expected Output: Text printed with bold red and bold green underlined styles respectively.

---

### Creating and Displaying Tables

```python
from rich.table import Table
from rich.console import Console

console = Console()
table = Table(title="User Info")

table.add_column("Name", style="cyan", no_wrap=True)
table.add_column("Age", style="magenta")
table.add_column("City", justify="right", style="green")

table.add_row("Alice", "30", "New York")
table.add_row("Bob", "25", "Los Angeles")

console.print(table)
```

Expected Output: A styled table with colored headers and aligned columns.

---

### Syntax Highlighting

```python
from rich.console import Console
from rich.syntax import Syntax

code = '''def greet(name):
    print(f"Hello, {name}!")
'''

console = Console()
syntax = Syntax(code, "python", theme="monokai", line_numbers=True)
console.print(syntax)
```

Expected Output: Python code rendered with Monokai color theme and line numbers.

---

### Progress Bar Example

```python
from rich.progress import track
import time

for step in track(range(10), description="Processing..."):
    time.sleep(0.5)
```

Expected Output: A progress bar with a description that updates dynamically.

---

### Live Output

```python
from rich.live import Live
from rich.table import Table
import time

table = Table()
table.add_column("Row ID")
table.add_column("Progress")

with Live(table, refresh_per_second=4):
    for i in range(10):
        table.add_row(str(i), f"{i*10}%")
        time.sleep(0.4)
```

Expected Output: A live-updating table in-place in the terminal.

---

## API Reference

### `Console`

The central class for printing styled content and managing terminal output.

- `print(*objects, style=None, **kwargs)`: Print rich text or renderables with optional styles.
- `clear()`: Clear the terminal screen.
- `input(prompt)`: Prompt for user input with rich formatted prompt.
- `status(text, spinner="dots")`: Context manager showing a status spinner.

### `Table`

A class representing tabular data with flexible configurations.

- `add_column(header: str, style: str = None, justify: str = None, no_wrap: bool = False)`: Adds a column.
- `add_row(*cells: str)`: Adds a row of data.

### `Syntax`

Renders syntax-highlighted source code.

- Constructor parameters:
  - `code` (str): Source code string.
  - `lexer_name` (str): Programming language name.
  - `theme` (str): Color theme.
  - `line_numbers` (bool): Show line numbers.
- `highlight(code: str)`: Static method to highlight code.

### `Progress`

Provides configurable progress bars with tasks and columns.

- `add_task(description, total=None)`: Adds a new task.
- `update(task_id, advance)`: Advances progress.
- `start()`, `stop()`: Control progress display.

### `Panel`

A container widget for grouping content with borders and title.

- Constructor parameters:
  - `renderable`: Content to display inside the panel.
  - `title`: Header text.
  - `border_style`: Style of the panel border.

### `Live`

Allows dynamic, live updating of terminal content.

- Used as a context manager wrapping a renderable.
- Supports manual refresh rate configuration.

### `Tree`

Visualizes hierarchical structures.

- `add(label, style=None)`: Adds a branch or leaf node.
- Supports nested nodes and customization.

### `traceback.install`

Installs enhanced tracebacks that replace standard Python tracebacks.

---

## Contributing

Rich welcomes contributions and improvements. To contribute:

1. Fork the repository on GitHub: [https://github.com/Textualize/rich](https://github.com/Textualize/rich).
2. Create a feature branch: `git checkout -b feature-name`.
3. Make your enhancements or fixes.
4. Ensure all tests pass and add new tests if applicable.
5. Submit a pull request with clear description.

Refer to the CONTRIBUTING.md file in the repo for detailed guidelines.

---

## License

Rich is licensed under the BSD-3-Clause License. See the [LICENSE](https://github.com/Textualize/rich/blob/master/LICENSE) file for details.

---

## Contactp

- GitHub Repository: [https://github.com/Textualize/rich](https://github.com/Textualize/rich)
- Issues and feature requests: Use the GitHub Issues page for the repository.
- Twitter: [@Textualize_io](https://twitter.com/Textualize_io)

```

```
