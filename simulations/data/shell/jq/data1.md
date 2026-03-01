# jq - Command-line JSON Processor

## Overview

`jq` is a powerful, flexible, and lightweight command-line tool designed for parsing, filtering, transforming, and outputting JSON data. It allows users to slice, filter, map, and transform structured JSON data with a concise and expressive programming language resembling functional programming.

### Domain Concepts

- **JSON (JavaScript Object Notation):** The primary data format that `jq` operates on. JSON is a common, text-based data interchange format.
- **Filters:** Expressions defining how to transform JSON data; these are the core building blocks of `jq` programs.
- **Streams:** `jq` can process JSON in a streaming fashion, which is efficient for large datasets.
- **Pipelines:** Composition of filters, where output from one filter becomes input to the next.
- **Modules:** Reusable collections of jq functions and filters.
- **Data Types:** Supported JSON types (objects, arrays, numbers, strings, booleans, null) and jq-specific constructs.
- **Operators:** Syntax elements for manipulating JSON including pipes, conditionals, arrays, objects, and more.

`jq` enhances workflows involving JSON manipulation by allowing complex data extraction and transformation tasks scripted via the command-line or embedded in shell scripts, CI pipelines, and programming environments.

---

## Installation

`jq` binaries are available for major platforms including Linux, macOS, and Windows.

### Using package managers

- **macOS (Homebrew):**

  ```bash
  brew install jq
  ```

- **Debian/Ubuntu:**

  ```bash
  sudo apt-get install jq
  ```

- **Fedora:**

  ```bash
  sudo dnf install jq
  ```

- **Windows (Chocolatey):**

  ```powershell
  choco install jq
  ```

### From source

Clone the repository and build with `make`:

```bash
git clone https://github.com/jqlang/jq.git
cd jq
./configure
make
sudo make install
```

---

## Usage and Examples

`jq` reads JSON from standard input or file and applies filters to transform it.

### Basic example: Pretty-print JSON

```bash
cat sample.json | jq .
```

### Selecting a field from JSON objects

Input JSON:

```json
{ "name": "Alice", "age": 30 }
```

Filter to get the name field:

```bash
echo '{ "name": "Alice", "age": 30 }' | jq '.name'
```

Output:

```
"Alice"
```

### Filtering arrays

Given an array of objects:

```json
[
  { "name": "Alice", "age": 30 },
  { "name": "Bob", "age": 25 }
]
```

Filter to select people older than 25:

```bash
jq '.[] | select(.age > 25)'
```

Output:

```json
{
  "name": "Alice",
  "age": 30
}
```

### Creating new JSON objects

```bash
echo '{"name": "Alice", "age": 30}' | jq '{personName: .name, ageNextYear: (.age + 1)}'
```

Output:

```json
{
  "personName": "Alice",
  "ageNextYear": 31
}
```

### Combining filters and pipes

```bash
jq '.[] | {name: .name, decade: (.age / 10 | floor * 10)}' people.json
```

This creates a new object for each person with their name and the decade of their age.

---

## API Reference

`jq` primarily operates as a command-line program, but also exposes an API for embedding and extending.

### Command-line Usage

```bash
jq [options] <jq filter> [file...]
```

- `<jq filter>`: The core JSON-processing expression.
- `[file...]`: One or more JSON files. If omitted, reads from standard input.

### Common options

- `-c` : Compact output (each JSON entity on one line).
- `-r` : Output raw strings, not JSON.
- `-s` : Read all inputs into an array and process once.
- `-f <file>` : Read filter from a file instead of command line.
- `--arg name value` : Set a string variable for use in the filter.
- `--argjson name value` : Set a JSON variable for use in the filter.
- `-M` : Monochrome output (disables colorization).
- `--sort-keys` : Alphabetically sort keys in output JSON objects.

---

### Embedding API (libjq)

`jq` provides a C API to embed its engine into other applications, documented in the `src` folder API headers.

Key functions:

- `jq_init()`: Creates a new jq state.
- `jq_compile(jq_state *, const char *program)`: Compiles a jq filter program.
- `jq_start(jq_state *, jv input, int flags)`: Executes compiled filter on input.
- `jq_next(jq_state *)`: Returns next output from jq evaluation.
- `jq_teardown(jq_state *)`: Frees jq state and resources.

---

## Usage Patterns

- **Filtering JSON by keys:** Use `.key` or `.["key"]` to retrieve specific values.
- **Filtering array elements:** Use `.[]` to iterate elements.
- **Selecting elements:** Use `select(<condition>)` to filter items based on conditions.
- **Object construction:** Use `{key: value, ...}` syntax to make new JSON objects.
- **Pipelines:** Compose filters using `|` to transform data step-by-step.
- **Functions:** Use built-in jq functions for string manipulation, math, and more.
- **Variables:** Pass variables from command line with `--arg` or `--argjson` for dynamic queries.

---

## Contributing

Contributions are welcome! To participate:

1. Fork the `jq` repository on GitHub.
2. Create a new branch for your feature or bugfix.
3. Develop your feature following the coding style.
4. Include tests for any new functionality.
5. Submit a pull request with a clear description.

For major changes, please open an issue for discussion first.

---

## License

`jq` is distributed under the MIT License. See the [LICENSE](https://github.com/jqlang/jq/blob/master/LICENSE) file for details.

---

## Contact

- Repository: https://github.com/jqlang/jq
- Issues: https://github.com/jqlang/jq/issues
- Maintainers and contributors can be contacted via the GitHub repository.

---
