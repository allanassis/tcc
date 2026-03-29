# jq

## Overview

`jq` is a lightweight and flexible command-line JSON processor. It allows users to slice, filter, map, and transform structured JSON data with ease. As a domain-specific language and tool designed for querying and manipulating JSON, `jq` brings powerful expressions inspired by functional programming, enabling complex data extraction and transformation workflows in shell environments.

The main domain concepts of `jq` include:

- **JSON:** JavaScript Object Notation, a lightweight data interchange format that `jq` operates upon.
- **Filters:** Expressions that transform JSON inputs by selecting, altering, or generating new JSON values.
- **Streams:** Inputs and outputs in JSON format, supporting processing of large or continuous data.
- **Operators and Functions:** Built-in constructs for manipulation, arithmetic, logic, and data access.
- **Modules:** Packages of functions and definitions that extend `jq`'s capabilities and enable code reuse.
- **Pipelines:** Chaining of filters to perform complex transformations step-by-step.

`jq` is widely used in scripting, automation, data parsing, REST API interactions, and anywhere JSON processing is required on the command line.

---

## Installation

`jq` can be installed on various platforms:

### Linux

Using package managers:

- Debian/Ubuntu:

  ```bash
  sudo apt-get install jq
  ```

- Fedora:

  ```bash
  sudo dnf install jq
  ```

- Arch Linux:

  ```bash
  sudo pacman -S jq
  ```

### macOS

Using Homebrew:

```bash
brew install jq
```

### Windows

- Download precompiled binaries from the official jq website: https://stedolan.github.io/jq/download/

- Alternatively, install via package managers like Chocolatey:

  ```bash
  choco install jq
  ```

### Build from Source

Clone the repository and build using make:

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

`jq` reads JSON from standard input and writes the result to standard output. The core usage pattern is:

```bash
jq [options] <filter> [file...]
```

### Example 1: Pretty-print JSON

```bash
cat data.json | jq .
```

Output is formatted, indented JSON for easy reading.

### Example 2: Extract object fields

Given input:

```json
{ "name": "Alice", "age": 30, "city": "Wonderland" }
```

Run:

```bash
jq '.name' input.json
```

Output:

```json
"Alice"
```

### Example 3: Filter arrays

Input:

```json
[
  { "name": "Alice", "age": 30 },
  { "name": "Bob", "age": 25 }
]
```

Get names of persons older than 26:

```bash
jq '.[] | select(.age > 26) | .name' input.json
```

Output:

```json
"Alice"
```

### Example 4: Modify JSON objects

Add new field:

```bash
jq '. + { "country": "Wonderland" }' input.json
```

### Example 5: Using jq programmatically in shell scripts

```bash
value=$(jq -r '.name' input.json)
echo "Name is $value"
```

---

## API Reference

### Command-Line Options

- `-c`, `--compact-output`

  Output JSON in compact form (no extra whitespace).

- `-r`, `--raw-output`

  Output raw strings, not JSON encoded.

- `-s`, `--slurp`

  Read entire input stream into a large array and apply filter once.

- `-f program-file`, `--from-file program-file`

  Load filter program from a file.

- `--arg name value`

  Pass a string value as a variable to `jq`.

- `--argjson name value`

  Pass a JSON value as a variable.

- `-n`, `--null-input`

  Use `null` as the input instead of reading.

- `-e`, `--exit-status`

  Exit with status 1 if filter output is false or null.

- `--version`

  Show version and exit.

---

### Filters and Functions

- Basic filter syntax: This is the core component where JSON is queried and transformed.

- `.` (dot)

  Represents the current input.

- `.foo`

  Access field `foo` of an object.

- `.[]`

  Iterates over elements of an array.

- `select(condition)`

  Filters elements that satisfy the condition.

- Arithmetic: `+`, `-`, `*`, `/`, `%`

- Comparisons: `==`, `!=`, `>`, `<`, `>=`, `<=`

- Logical: `and`, `or`, `not`

- `map(f)`

  Applies filter `f` to each element in an array.

- `reduce`

  Reduces elements using a reducer function.

- String functions: `length`, `startswith`, `endswith`, `contains`.

- Array functions: `length`, `index`, `sort`, `unique`.

- `input`, `inputs`

  Read JSON inputs separately or as multiple streams.

---

### Execution Facts

- Filters are applied to each JSON input element in a streaming fashion.

- Filter outputs can modify, project or generate JSON values.

- Variables passed at command invocation are accessible inside filters via `$name`.

- If the filter produces multiple outputs, each is printed on its own line.

- Program files can contain function definitions for reuse.

- `jq` expressions can be composed by piping filters together with the pipe operator `|`.

---

## License

`jq` is released under the MIT License. See the LICENSE file at https://github.com/jqlang/jq/blob/master/LICENSE for details.
