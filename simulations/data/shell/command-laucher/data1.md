# command-launcher

## Overview

`command-launcher` is a lightweight Python tool designed to simplify running shell commands and scripts with advanced control over their execution. It provides an easy-to-use interface to launch external commands or scripts programmatically from Python, capturing their output, handling errors, and managing execution flow.

The main domain concepts modeled by `command-launcher` include:

- **Command Execution:** Running external system commands or scripts.
- **Process Management:** Monitoring running commands, capturing standard output and error streams.
- **Execution Control:** Supporting synchronous and asynchronous execution, timeout management.
- **Result Handling:** Retrieving command exit codes, output text, and raising exceptions on command failures.

`command-launcher` allows developers to embed robust command execution logic within their Python applications, scripts, or automation workflows in a consistent and reliable manner.

---

## Installation

You can install `command-launcher` via pip:

```bash
pip install command-launcher
```

Ensure you have Python 3.6 or higher installed.

---

## Usage and Examples

### Running a Simple Command

```python
from command_launcher import run

result = run("echo Hello, world!")
print(result.stdout)  # Outputs: Hello, world!
print(result.returncode)  # Outputs: 0 for success
```

### Running a Command with Timeout and Error Check

```python
from command_launcher import run, CommandExecutionError

try:
    result = run("sleep 5", timeout=2)
except CommandExecutionError as e:
    print(f"Command failed or timed out: {e}")
```

### Running a Command Asynchronously

```python
from command_launcher import run_async
import asyncio

async def main():
    proc = await run_async("ping -c 4 google.com")
    stdout, stderr = await proc.communicate()
    print(stdout.decode())

asyncio.run(main())
```

---

## API Reference

### `run(command: str, *, shell: bool = False, timeout: int = None, check: bool = False, cwd: str = None, env: dict = None) -> CompletedProcess`

Executes a command synchronously.

- `command` (str): The command to execute.
- `shell` (bool): Whether to execute the command through the shell.
- `timeout` (int or float): Time in seconds to wait for command completion before raising a timeout exception.
- `check` (bool): If True, raises `CommandExecutionError` if the command returns a non-zero exit status.
- `cwd` (str): The working directory where command will run.
- `env` (dict): Environment variables to use during execution.

Returns a `CompletedProcess` object with attributes:

- `args`: The command run.
- `returncode`: The exit code of the command.
- `stdout`: Captured standard output as a string.
- `stderr`: Captured standard error as a string.

Raises:

- `CommandExecutionError`: If `check=True` and the command fails.
- `TimeoutExpired`: If the command exceeds the specified timeout.

---

### `run_async(command: str, *, shell: bool = False, cwd: str = None, env: dict = None) -> asyncio.subprocess.Process`

Runs a command asynchronously.

- `command` (str): The command to execute.
- `shell` (bool): Execute command through shell.
- `cwd` (str): Working directory.
- `env` (dict): Environment variables.

Returns an `asyncio.subprocess.Process` instance.

---

### Exceptions

#### `CommandExecutionError`

Raised when a command fails with a non-zero exit code if `check=True` is specified in `run`.

Contains attributes:

- `returncode`: The exit code.
- `cmd`: The command attempted.
- `output`: Captured stdout.
- `stderr`: Captured stderr.

---

## Contributing

Contributions to improve functionality, add features, fix bugs, or enhance documentation are welcome.

- Fork the repository on GitHub.
- Create a feature branch.
- Submit pull requests with detailed descriptions.
- Ensure code clarity and test new features if applicable.

---

## License

`command-launcher` is available under the MIT License. See the [LICENSE](https://github.com/xZepyx/command-launcher/blob/master/LICENSE) file for details.

---

## Contact

- GitHub Repository: [https://github.com/xZepyx/command-launcher](https://github.com/xZepyx/command-launcher)
- Issues and feature requests: Use the repository's GitHub issues page.
