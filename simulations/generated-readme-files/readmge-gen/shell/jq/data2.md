# jq - Command-line JSON Processor

## Overview

`jq` is a lightweight and flexible command-line JSON processor. It allows users to parse, filter, transform, and output JSON data with ease using a simple but powerful query language. Designed for handling JSON data from files or standard input, `jq` excels in shell scripting and automation, enabling powerful JSON manipulation directly from the command line.

### Domain Concepts

- **JSON Data:** The ubiquitous data interchange format that `jq` processes.
- **Filters:** Expressions in jq's domain-specific language (DSL) used to extract or transform JSON data.
- **Pipelines:** Chained filters to perform stepwise transformations.
- **Streams:** Input and output of JSON strings that `jq` can consume or generate.
- **Slice and Dice:** Selecting parts of JSON objects and arrays.
- **Functions:** Built-in and user-defined to perform operations on JSON data.

`jq` models JSON manipulation concepts as filters and produces JSON outputs that can be further processed or consumed.

---

## Installation

`jq` is widely available and can be installed on major operating systems using popular package managers.

### macOS (using Homebrew)

```bash
brew install jq
```

### Ubuntu/Debian

```bash
sudo apt-get install jq
```

### Fedora

```bash
sudo dnf install jq
```

### Windows

- Download pre-built binaries from the official [jq releases page](https://github.com/stedolan/jq/releases).
- Use package managers such as [Chocolatey](https://chocolatey.org/packages/jq) or [Scoop](https://scoop.sh/).

---

## Usage and Examples

`jq` is used by providing JSON input and specifying filters to process the JSON.

### Basic Usage

```bash
jq <filter> <file>
```

- `<filter>`: jq expression to apply to JSON input.
- `<file>`: JSON file to process; omitting will read from standard input.

### Example 1: Extract a field from JSON object

Given `data.json`:

```json
{
  "name": "John",
  "age": 30
}
```

Command:

```bash
jq '.name' data.json
```

Output:

```json
"John"
```

### Example 2: Filter array elements

Given `data.json`:

```json
[
  { "name": "Alice", "age": 25 },
  { "name": "Bob", "age": 35 }
]
```

Command to select people older than 30:

```bash
jq '.[] | select(.age > 30)' data.json
```

Output:

```json
{
  "name": "Bob",
  "age": 35
}
```

### Example 3: Modify JSON data

Double the age field of each person:

```bash
jq 'map(.age = .age * 2)' data.json
```

Output:

```json
[
  { "name": "Alice", "age": 50 },
  { "name": "Bob", "age": 70 }
]
```

### Example 4: Read from standard input

```bash
echo '{"foo": 42}' | jq '.foo'
```

Output:

```
42
```

---

## API Reference

`jq`'s core interface is a command-line binary with extensive filter and options described below.

### Main Command-line Options

- `-c, --compact-output`

  Outputs JSON in compact form without extra whitespace.

- `-M, --monochrome-output`

  Disables color output.

- `-r, --raw-output`

  Outputs raw strings, not JSON-quoted.

- `-s, --slurp`

  Instead of running the filter for each JSON object in the input, read all inputs into an array and run the filter once.

- `-f <file>, --from-file <file>`

  Read filter program from a file instead of the command line.

- `-n, --null-input`

  Use `null` as the single input value.

---

### jq Filters and Functions

- **Filters:** Core unit of jq processing, applied to JSON input.

  Examples:
  - `.foo` — Extracts the `foo` property.
  - `.[]` — Iterate over array elements.
  - `select(condition)` — Selects elements where condition is true.
  - `map(f)` — Applies filter `f` to all elements of array.
  - `.` — Identity filter, outputs input unchanged.

- **Functions:** jq provides a rich set of built-in functions manipulating strings, numbers, arrays, objects, and more.

  E.g. `length`, `keys`, `has`, `split`, `gsub`.

---

### Example Filter Usage in Scripts

```bash
jq -r '.users[] | select(.active) | .email' users.json
```

This outputs raw emails of active users.

---

## Feedback and Debugging

- Use `jq`’s `--debug-dump` option to debug filter compilation.
- Use verbose logging with `jq --verbose`.
- `jq` outputs errors to stderr with descriptions of filter syntax or runtime issues.
- Check exit code to determine success (`0`) or failure (`>0`).

---

## License

`jq` is licensed under the MIT License. See the [LICENSE file](https://github.com/jqlang/jq/blob/main/LICENSE) for details.
