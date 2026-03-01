# jq

## Overview

`jq` is a powerful, lightweight, and flexible command-line JSON processor designed for filtering, transforming, and extracting data from JSON documents. It allows developers and system administrators to manipulate JSON with a simple yet expressive query language inspired by functional programming concepts. `jq` is invaluable for working with JSON data streams, automating data processing tasks, and integrating JSON transformations in shell scripts and pipelines.

### Domain Concepts

- **JSON (JavaScript Object Notation):** The primary data format `jq` processes. JSON is a text-based, language-independent data interchange format.
- **Filters:** The core concept in `jq`, which are expressions that describe how to transform or extract data from JSON inputs.
- **Streams and Pipelines:** `jq` operates on JSON streams, allowing chaining of filters to build complex data transformations.
- **Functional Programming:** `jq` embraces functional programming paradigms such as composing, mapping, and reducing data.
- **Modules and Functions:** Extensible parts of `jq` scripts that allow reuse and modularization of logic.
- **Output Formats:** JSON by default, but with options to format output as raw strings, compact, or pretty-printed JSON.

---

## Installation

`jq` is available on multiple platforms and can be installed via package managers or by downloading precompiled binaries.

### Using package managers

- **macOS (Homebrew):**

  ```bash
  brew install jq
  ```

- **Ubuntu / Debian:**

  ```bash
  sudo apt-get install jq
  ```

- **Fedora:**

  ```bash
  sudo dnf install jq
  ```

- **Windows:**

  Download the Windows executable from the official site [stedolan.github.io/jq/download](https://stedolan.github.io/jq/download)

### Building from source

Clone the repository and compile with `make`:

```bash
git clone https://github.com/jqlang/jq.git
cd jq
autoreconf -fi      # Generate configuration scripts
./configure
make
sudo make install
```

---

## Usage and Examples

`jq` reads JSON from standard input and applies filters to produce desired output.

### Basic usage

```bash
echo '{"name": "Alice", "age": 30}' | jq '.name'
```

Output:

```
"Alice"
```

### Common usage patterns

- **Extract a field:**

  ```bash
  jq '.fieldName' input.json
  ```

- **Pipe JSON output to another jq filter:**

  ```bash
  cat file.json | jq '.items[] | .id'
  ```

- **Filter objects matching a condition:**

  ```bash
  jq '.[] | select(.active == true)' data.json
  ```

- **Transform JSON structure:**

  ```bash
  jq '{users: .items | map({user_id: .id, email: .email})}' data.json
  ```

- **Pretty-print JSON:**

  ```bash
  jq '.' file.json
  ```

- **Raw output (no JSON quoting):**

  ```bash
  echo '{"name": "Alice"}' | jq -r '.name'
  ```

### Using jq in shell scripts

```bash
#!/bin/bash
result=$(curl -s https://api.example.com/data | jq -r '.items[0].name')
echo "First item name: $result"
```

---

## API Reference

`jq` core functionality is accessed via CLI commands and a C API for embedding, but primarily users interact via filters described below:

### Command-line interface (CLI)

```bash
jq [options] <filter> [file...]
```

- **filter**: The jq filter expression to apply.
- **file**: Input JSON file(s). Defaults to standard input if omitted.

### Common options

- `-r` / `--raw-output`: Output raw strings, not JSON-encoded.
- `-c` / `--compact-output`: Output JSON in compact form (no pretty-print).
- `-s` / `--slurp`: Instead of processing each JSON entity independently, read all inputs into an array and process once.
- `-f <file>` / `--from-file <file>`: Read filter expression from file.
- `--arg name value`: Pass string variables into the jq program.
- `--argjson name value`: Pass JSON variables into the jq program.

### Filter Language Highlights

- **Literal values:** Strings, numbers, booleans, null.
- **Object and array constructors:** `{key: value}`, `[value1, value2]`
- **Path selectors:** `.`, `.key`, `.[index]`
- **Functions:** e.g. `length`, `map`, `select`, `sort`, `contains`
- **Conditionals:** `if ... then ... else ... end`
- **Pipes:** `|` chaining of filters
- **Variables and parameters:** `$var` usage

---

## Contributing

The `jq` project welcomes contributions from the community to enhance its filter language, improve performance, fix bugs, and extend supported platforms.

### How to contribute

- Fork the repository on GitHub: [https://github.com/jqlang/jq](https://github.com/jqlang/jq)
- Clone your fork and create a feature branch.
- Build and test your changes thoroughly.
- Add tests for new features or bug fixes.
- Submit pull requests with clear explanations.
- Follow coding and style guidelines described in the CONTRIBUTING.md file.

### Development setup

- Requires autotools for building (`autoreconf`, `./configure`).
- Use existing test suite with `make test` after building.
- Contributions should maintain cross-platform compatibility.

---

## License

`jq` is distributed under the MIT License. See the [LICENSE](https://github.com/jqlang/jq/blob/master/LICENSE) file for details.

---

## Contact

- **Repository:** [https://github.com/jqlang/jq](https://github.com/jqlang/jq)
- **Issue Tracker:** Use GitHub Issues for bug reports and feature requests.
- **Mailing List and IRC:** Refer to the official website for community communication channels.
- **Author:** Stephen Dolan and contributors

For more information and documentation, visit the official website: [https://stedolan.github.io/jq/](https://stedolan.github.io/jq/)
