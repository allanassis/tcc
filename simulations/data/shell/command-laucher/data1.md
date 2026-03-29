# Command Launcher

## Overview

Command Launcher is a lightweight Python tool designed to simplify and automate the execution of command-line tasks. It acts as a command dispatcher that allows users to define and run shell commands with structured argument parsing and environment management. The tool helps users automate repetitive CLI workflows, manage environment variables, and organize commands for easy reuse and execution.

### Domain Concepts

- **Command Registration:** Defines shell commands with associated parameters and metadata.
- **Argument Parsing:** Uses structured schemas to parse and validate command-line input arguments.
- **Execution Environment:** Supports setting and managing environment variables and contextual information.
- **Command Execution:** Runs shell commands with controlled input, output, error handling, and status reporting.
- **Extensibility:** Designed so new commands can be added as Python functions decorated or registered to the launcher.

---

## Installation

To use Command Launcher, you need Python 3.7 or higher.

Install via pip:

```bash
pip install command-launcher
```

Alternatively, clone the repository and install with:

```bash
git clone https://github.com/xZepyx/command-launcher.git
cd command-launcher
pip install .
```

---

## Usage and Examples

### Basic Usage

Commands are registered internally and can be invoked via the command launcher CLI:

```bash
command-launcher <command> [options] [arguments]
```

Example to list available commands:

```bash
command-launcher --help
```

### Defining a Command (Usage Pattern)

Commands are Python functions decorated or registered with the launcher. For example:

```python
from command_launcher import CommandLauncher, argument

launcher = CommandLauncher()

@launcher.command('greet')
@argument('name', type=str, help='Name to greet')
def greet_command(name):
    print(f"Hello, {name}!")

if __name__ == '__main__':
    launcher.run()
```

Run the command from terminal:

```bash
python myscript.py greet --name John
```

Expected output:

```
Hello, John!
```

### Running Shell Commands

You can define commands to execute shell instructions via the launcher environment with support for environment variables and input/output redirection.

---

## API Reference

### `CommandLauncher`

Primary class to register and manage command functions.

- `command(name: str)` (decorator): Registers a function as a CLI command.
- `run(args: list = None)`: Parses input arguments and executes corresponding command.

### `argument`

Decorator to define command arguments with validation and help.

- Parameters:
  - `name` (str): Argument name.
  - `type` (type): Argument data type (e.g., `str`, `int`, `bool`).
  - `default` (optional): Default value if argument is omitted.
  - `help` (str): Help text shown in usage.

### Command Functions

- Command functions accept arguments as Python parameters matching defined arguments.
- Can perform any logic, including shell command invocation within Python.

---

## License

Command Launcher is licensed under the MIT License. See the [LICENSE](https://github.com/xZepyx/command-launcher/blob/master/LICENSE) file for details.
