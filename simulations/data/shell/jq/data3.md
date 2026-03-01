# jq

## Overview

`jq` is a powerful, flexible, and lightweight command-line JSON processor. It allows developers and system administrators to parse, filter, transform, and output JSON data easily from shell scripts or command line operations. Modeled after the syntax of sed and awk but designed specifically for JSON, `jq` provides a user-friendly way to handle JSON data using a simple but expressive domain-specific language.

### Domain Concepts

- **JSON Data Structures**: `jq` operates on JSON data, including objects, arrays, strings, numbers, booleans, and null.
- **Filters**: Core building blocks in `jq` that process and transform JSON inputs into desired outputs.
- **Pipelines & Composition**: Filters can be combined and chained to create complex transformations.
- **Programmatic Querying**: A rich language enables selecting, updating, reducing, and producing new JSON data.
- **Streaming Support**: Process large JSON inputs incrementally without loading them entirely in memory.
- **Built-in Functions and Operators**: Provide arithmetic operations, string manipulation, conditionals, and more.

`jq` is widely used for inspecting logs, configuring infrastructure as code, data extraction, and integration workflows.

---

## Installation

### Prerequisites

- Works on Unix/Linux, macOS, and Windows platforms.
- Requires a terminal or command prompt to run.

### Installation Methods

#### Linux (using package managers):

```bash
sudo apt-get install jq       # Debian/Ubuntu
sudo yum install jq           # RHEL/CentOS/Fedora
```

#### macOS (using Homebrew):

```bash
brew install jq
```

#### Windows

- Download precompiled binaries from https://stedolan.github.io/jq/download/
- Alternatively, install via Chocolatey package manager:

```powershell
choco install jq
```

### Build from Source

Clone the repository and build manually:

```bash
git clone https://github.com/jqlang/jq.git
cd jq
autoreconf -i
./configure
make
sudo make install
```

---

## Usage and Examples

`jq` reads JSON from standard input and outputs results based on filter expressions.

### Basic Syntax

```bash
jq <filter> <file>
```

If no file is specified, JSON is read from standard input.

### Example 1: Pretty-print JSON

```bash
jq '.' data.json
```

Outputs formatted JSON for easy reading.

### Example 2: Extract a field from an object

Given JSON:

```json
{
  "name": "Alice",
  "age": 30,
  "city": "Wonderland"
}
```

Command:

```bash
jq '.name' data.json
```

Output:

```json
"Alice"
```

### Example 3: Filtering array elements

JSON:

```json
[
  { "name": "Alice", "age": 30 },
  { "name": "Bob", "age": 25 },
  { "name": "Carol", "age": 27 }
]
```

Filter:

```bash
jq '.[] | select(.age > 26)' data.json
```

Output:

```json
{
  "name": "Alice",
  "age": 30
}
{
  "name": "Carol",
  "age": 27
}
```

### Example 4: Using variables and functions

```bash
jq --arg city "Wonderland" '.city == $city' data.json
```

Returns `true` if the city matches.

---

## API Reference

The core of `jq` is its Filter language, which can be used interactively or embedded.

### Main Filters

- `.` — Identity operator; returns input as is.
- `.key` — Gets the value of "key" in a JSON object.
- `.[]` — Iterates over elements of an array.
- `select(condition)` — Filters elements based on condition.
- `map(f)` — Applies filter `f` to each element of an array.
- `reduce stream as $var (...)` — Reduces input stream to a summary value.
- `length` — Returns length of string or array.
- `sort`, `sort_by(f)` — Sort arrays.
- `if`, `then`, `else`, `end` — Conditional expressions.
- `try`, `catch` — Error handling inside filters.

### Built-in Functions

- String operations: `startswith`, `endswith`, `match`, `split`, `capture`.
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `//` (alternative)
- Logical: `and`, `or`, `not`
- Type tests: `type`, `has(key)`, `inside`
- JSON construction: `tojson`, `fromjson`

### Command-Line Options

- `-c`, `--compact-output`: Output JSON in compact form.
- `-r`, `--raw-output`: Output raw strings, not JSON encoded.
- `-s`, `--slurp`: Read entire input into an array.
- `-f <file>`: Read filter from a file.
- `--arg name value`: Pass string variable.
- `--argjson name value`: Pass JSON variable.
- `--stream`: Parse input in streaming fashion.

### Exit Codes

- `0` on success.
- Non-zero on errors (failed parse, runtime errors).

---

## Contributing

`jq` welcomes contributions that improve functionality, documentation, and test coverage.

To contribute:

1. Fork the repository on GitHub.
2. Create a feature branch.
3. Implement and test your changes.
4. Submit a pull request with clear explanations and tests.

Refer to the official contribution guidelines on the GitHub repository.

---

## License

`jq` is licensed under the MIT License. See [LICENSE](https://github.com/jqlang/jq/blob/master/LICENSE) for details.

---

## Contact

- Official Repository: https://github.com/jqlang/jq
- Website: https://stedolan.github.io/jq/
- Issues: https://github.com/jqlang/jq/issues
- Maintainer: Stephen Dolan and community contributors

For questions or support, use the GitHub issue tracker or community forums.
