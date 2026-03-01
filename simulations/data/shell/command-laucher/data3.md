# Command Launcher

## Overview

Command Launcher is a lightweight Python utility that facilitates running shell commands interactively or programmatically, providing easy execution with controlled output handling. Its primary function is to allow users to launch system commands, capture their outputs, and manage command execution flow within Python scripts or interactive sessions.

The key domain concepts in Command Launcher include:

- **Shell Command Execution:** Running system shell commands from Python.
- **Process Management:** Starting and managing subprocesses with optional output capture.
- **Output Handling:** Accessing standard output and standard error streams from commands.
- **Return Codes:** Checking process exit status for success or failure.
- **Interactive and Scripted Use:** Facilitating command execution both manually and in automated workflows.

Command Launcher abstracts away common boilerplate for subprocess management, making it simpler and more consistent to run commands from Python environments.

---

## Installation

### Prerequisites

- Python 3.6 or higher is recommended.

### Installing via pip

You can install Command Launcher from PyPI using:

```bash
pip install command-launcher
```

### Installing from source

Clone the repository and install locally:

```bash
git clone https://github.com/xZepyx/command-launcher.git
cd command-launcher
pip install .
```

---

## Usage and Examples

### Running a Simple Command

```python
from command_launcher import CommandLauncher

# Create an instance of CommandLauncher
launcher = CommandLauncher()

# Run a command and get output
result = launcher.run("echo Hello World")

print(result.stdout)  # Expected: Hello World
print(result.returncode)  # Expected: 0
```

### Running a Command with Error Handling

```python
result = launcher.run("ls /nonexistentfolder")

if result.returncode != 0:
    print("Error:", result.stderr)
```

### Running Commands Interactively with Real-time Output

```python
# Run a long-running command and stream output live
launcher.run_interactive("ping -c 4 google.com")
```

---

## API Reference

### `CommandLauncher` Class

The main class to launch and manage shell commands.

#### Methods

- `run(command: str, capture_output: bool = True, shell: bool = True) -> CompletedProcess`

  Executes the provided command string.
  - **Parameters:**
    - `command` (str): Command line string to execute.
    - `capture_output` (bool, optional): Whether to capture stdout and stderr. Defaults to True.
    - `shell` (bool, optional): Whether to run the command through the shell. Defaults to True.

  - **Returns:**
    - A `CompletedProcess` object with attributes:
      - `returncode` (int): Exit status of the command.
      - `stdout` (str or bytes): Captured standard output.
      - `stderr` (str or bytes): Captured standard error.

- `run_interactive(command: str) -> None`

  Runs the command interactively, streaming output to the console in real-time.
  - **Parameters:**
    - `command` (str): Command line string to execute interactively.

  - **Returns:** None

---

## Contributing

Contributions to Command Launcher are welcome. You can help by:

- Reporting issues on the GitHub repository.
- Submitting pull requests with improvements or bug fixes.
- Adding tests or improving documentation.

To contribute:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with descriptive messages.
4. Submit a pull request for review.

Please follow the code style and write tests where applicable.

---

## License

Command Launcher is licensed under the MIT License. See the LICENSE file in the repository for details.

---

## Contact

- GitHub Repository: [https://github.com/xZepyx/command-launcher](https://github.com/xZepyx/command-launcher)

For issues or feature requests, please use the GitHub Issues page.
