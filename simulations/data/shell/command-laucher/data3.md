# command-launcher

## Overview

`command-launcher` is a simple Node.js utility designed to facilitate launching external commands or executable files from JavaScript code. This tool provides an easy-to-use interface for running system commands, handling their output, and managing command execution in an asynchronous and controlled manner. It is especially useful for developers who want to automate or integrate command line processes within their Node.js applications.

### Domain Concepts

- **Command Execution:** Running shell commands or executables from a script.
- **Process Management:** Handling asynchronous command execution, capturing standard output, standard error, and managing exit codes.
- **Cross-Platform Compatibility:** Ensuring commands execute correctly on supported operating systems.
- **Callback and Promise APIs:** Supporting both callback functions and Promises for handling command execution results.

---

## Installation

Ensure you have [Node.js](https://nodejs.org/) installed.

Install the package via npm:

```bash
npm install command-launcher
```

or using yarn:

```bash
yarn add command-launcher
```

The package supports Node.js 10 or later and runs on major platforms where Node.js is supported.

---

## Usage and Examples

### Basic Usage with Callbacks

```js
const commandLauncher = require("command-launcher");

commandLauncher("ls", ["-l", "/usr"], (error, stdout, stderr) => {
  if (error) {
    console.error("Execution error:", error);
    return;
  }
  console.log("Standard Output:\n", stdout);
  if (stderr) {
    console.error("Standard Error:\n", stderr);
  }
});
```

This example runs the `ls -l /usr` command and prints the output or any errors.

### Usage with Promises

The command-launcher also supports Promises for async/await usage:

```js
const commandLauncher = require("command-launcher");

async function runCommand() {
  try {
    const { stdout, stderr } = await commandLauncher.exec("node", [
      "--version",
    ]);
    console.log("Node version:", stdout);
    if (stderr) {
      console.error("Error output:", stderr);
    }
  } catch (err) {
    console.error("Failed to execute command:", err);
  }
}

runCommand();
```

### Running Commands Synchronously

If synchronous execution is needed (blocking the event loop), use the synchronous API:

```js
const commandLauncher = require("command-launcher");

try {
  const result = commandLauncher.execSync("echo", ["Hello World"]);
  console.log("Output:", result.toString());
} catch (error) {
  console.error("Sync execution failed:", error);
}
```

---

## API Reference

### `commandLauncher(command: string, args?: string[], callback?: function)`

Executes the specified command as a child process asynchronously.

- **Parameters:**
  - `command` (string): The executable or command line tool to run.
  - `args` (string[], optional): Array of string arguments to pass to the command.
  - `callback` (function, optional): Function called when execution completes with parameters `(error, stdout, stderr)`.

- **Returns:** A child process instance if no callback is provided.

### `commandLauncher.exec(command: string, args?: string[]): Promise<{stdout: string, stderr: string}>`

Executes a command asynchronously and returns a Promise.

- **Parameters:**
  - `command` (string): The executable or command line tool.
  - `args` (string[], optional): Arguments array.

- **Returns:** Promise resolving to an object containing `stdout` and `stderr`.

### `commandLauncher.execSync(command: string, args?: string[]): Buffer`

Executes the command synchronously.

- **Parameters:**
  - `command` (string): The executable or command line tool.
  - `args` (string[], optional): Arguments array.

- **Returns:** `Buffer` with the command output.

- **Throws:** Error on failure.

---

## License

This project is distributed under the MIT License. See the [LICENSE](https://github.com/xZepyx/command-launcher/blob/master/LICENSE) file for details.
