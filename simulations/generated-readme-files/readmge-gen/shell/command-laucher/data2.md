# command-launcher

## Overview

`command-launcher` is a lightweight Python library designed to simplify running shell commands from within Python scripts. It provides a clean, Pythonic interface for executing external commands and capturing their output, status, and errors. This tool is especially useful for scripting automation, workflow orchestration, or any scenario where interaction with the system shell is required.

### Domain Concepts

- **Command Execution:** Running shell commands or external programs from Python.
- **Process Management:** Starting and handling subprocesses with control over input/output.
- **Result Handling:** Capturing the standard output (stdout), standard error (stderr), and exit status of commands.
- **Timeouts:** Ability to limit the execution time of the commands.

These core concepts allow the user to integrate shell command functionality seamlessly into Python applications, encouraging robust error handling and output processing.

---

## Installation

To install the `command-launcher` package, you can use `pip`:

```bash
pip install command-launcher
```

Make sure you have Python 3.6 or later installed.

---

## Usage and Examples

### Basic Usage Example

To run a simple shell command and get its output:

```python
from command_launcher import CommandLauncher

# Initialize the launcher
launcher = CommandLauncher()

# Run a command
result = launcher.run("echo Hello, World!")

# Access the output
print("Standard Output:", result.stdout)
print("Standard Error:", result.stderr)
print("Exit Code:", result.exit_code)
```

**Expected output:**

```
Standard Output: Hello, World!

Standard Error:
Exit Code: 0
```

### Example: Running a Command with a Timeout

```python
result = launcher.run("sleep 5", timeout=2)
if result.timed_out:
    print("The command timed out.")
else:
    print("Command completed successfully.")
```

This example demonstrates how to run a command with a timeout, handling cases where the command takes too long.

### Example: Running Commands with Input Data

```python
result = launcher.run("cat", input_data="Hello from stdin\n")
print(result.stdout)
```

This pipes the string `"Hello from stdin\n"` to the command's standard input.

---

## API Reference

### `CommandLauncher` class

The main class to execute shell commands.

#### Methods

- `run(command: str, timeout: Optional[int] = None, input_data: Optional[str] = None) -> CommandResult`

Executes a shell command.

**Parameters:**

- `command` (str): The shell command to execute.
- `timeout` (int, optional): Number of seconds to wait before timing out the command.
- `input_data` (str, optional): Data to send to the standard input of the command.

**Returns:**

- `CommandResult`: An object containing execution results.

---

### `CommandResult` class

Represents the outcome of a command executed by `CommandLauncher`.

#### Attributes

- `stdout` (str): Standard output captured from the command.
- `stderr` (str): Standard error output captured.
- `exit_code` (int): The exit status code returned by the command.
- `timed_out` (bool): Indicates whether the command was terminated due to timeout.

---

## License

This project is licensed under the MIT License. See the [LICENSE](https://github.com/xZepyx/command-launcher/blob/master/LICENSE) file for details.
