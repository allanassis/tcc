# Command Launcher

## Overview

Command Launcher is a Python utility designed to facilitate executing shell commands asynchronously with easy management and improved workflow integration. It focuses on providing a simple yet powerful abstraction for launching commands, handling outputs, and monitoring execution results. The tool particularly benefits developers and system administrators who automate shell tasks or scripts within Python environments.

### Domain Concepts

- **Command Execution:** Running system shell commands or scripts programmatically.
- **Async Process Handling:** Managing asynchronous operations and retrieving outputs without blocking.
- **Output and Error Management:** Capturing command stdout and stderr for logging and processing.
- **Command Monitoring:** Tracking the state and result of executed commands.

---

## Installation

You can install Command Launcher via pip:

```bash
pip install command-launcher
```

Alternatively, clone the repository and install dependencies manually:

```bash
git clone https://github.com/xZepyx/command-launcher.git
cd command-launcher
pip install -r requirements.txt
```

The package requires Python 3.6 or newer.

---

## Usage and Examples

### Basic Usage

Use Command Launcher to execute a shell command asynchronously and retrieve its output.

```python
from command_launcher import Command

# Create a Command instance with the shell command.
cmd = Command("ls -la")

# Run the command asynchronously.
cmd.run()

# Wait for completion and get the output.
output = cmd.get_output()
print("Command output:", output)
```

### Advanced Usage: Running Multiple Commands

You can launch multiple commands and monitor their execution status individually.

```python
from command_launcher import Command
import time

cmd1 = Command("echo 'Hello World'")
cmd2 = Command("sleep 2 && echo 'Done sleeping'")

cmd1.run()
cmd2.run()

# Poll commands for completion
while not cmd1.is_finished() or not cmd2.is_finished():
    print("Waiting for commands to finish...")
    time.sleep(1)

print("Cmd1 output:", cmd1.get_output())
print("Cmd2 output:", cmd2.get_output())
```

---

## API Reference

### `Command(command_string, shell=True)`

Creates a new Command instance.

- **Parameters:**
  - `command_string` (str): The shell command to execute.
  - `shell` (bool, optional): Use shell execution; default is `True`.

### Methods

- `run()`

  Launches the command asynchronously. Non-blocking call.

- `get_output() -> str`

  Returns the standard output produced by the command after completion.

- `get_error() -> str`

  Returns the standard error output from the command.

- `is_finished() -> bool`

  Checks if the command execution has finished.

- `wait(timeout=None)`

  Blocks until the command finishes or until an optional timeout (in seconds).

- `terminate()`

  Sends a termination signal to the running command.

### Execution Facts

- The command runs asynchronously once `run()` is called.
- Calling `get_output()` or `get_error()` before completion may yield partial or empty results.
- Use `is_finished()` or `wait()` to synchronize before accessing outputs.
- `terminate()` can interrupt the running command but may not guarantee immediate stop depending on the underlying OS.

---

## Contributing

Contributions, bug reports, and feature requests are welcome. To contribute:

1. Fork the repository.
2. Create a feature branch.
3. Commit your changes with clear message.
4. Submit a pull request.

Please ensure your code adheres to existing style and includes tests where applicable.

---

## License

This project is licensed under the MIT License. See the LICENSE file in the repository for details.

---

## Contact

- GitHub Repository: [https://github.com/xZepyx/command-launcher](https://github.com/xZepyx/command-launcher)
- Issues and feature requests via GitHub Issues page.
