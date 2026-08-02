# jq

## Overview

`jq` is a powerful and flexible command-line JSON processor. It allows users to slice, filter, map, and transform structured JSON data with a concise and expressive functional programming language designed specifically for JSON. Using `jq`, developers and data analysts can parse, extract, and manipulate JSON data efficiently in a way similar to how `sed`, `awk`, and `grep` operate on text.

### Domain Concepts

- **JSON Data:** Textual format for structured data, composed of objects, arrays, strings, numbers, booleans, and nulls.
- **Filters:** Queries expressed in the `jq` language to transform and extract data from JSON.
- **Pipelines and Composition:** Combining filters to build complex queries step-by-step.
- **Streaming Processing:** Handling large JSON data efficiently with minimal memory usage.
- **Functions and Operators:** Built-in and user-defined functions for data transformations.
- **Variables and Assignments:** Managing data flow and intermediate states within queries.
- **Modules:** Encapsulated reusable code segments for extending functionality.

The main goal of `jq` is to provide a lightweight tool and language for transforming JSON data on the command line or in scripts, making it an essential tool for data processing pipelines, system administration, and rapid JSON data interrogation.

---

## Installation

`jq` is widely supported on multiple platforms including Linux, macOS, and Windows.

### On Linux

Use your system's package manager:

```bash
# Debian/Ubuntu
sudo apt-get install jq

# Fedora
sudo dnf install jq

# Arch Linux
sudo pacman -S jq
```

### On macOS

Install via Homebrew:

```bash
brew install jq
```

### On Windows

Download precompiled binaries from the official [jq releases](https://github.com/stedolan/jq/releases) page, or install via [chocolatey](https://chocolatey.org/packages/jq):

```powershell
choco install jq
```

### From Source

Clone the repository and build from source:

```bash
git clone https://github.com/stedolan/jq.git
cd jq
autoreconf -i
./configure
make
sudo make install
```

---

## Usage and Examples

`jq` is primarily used by passing JSON input through standard input (`stdin`) or from a file, combined with filter expressions.

### Basic Usage

```bash
jq '<filter>' <input-file>
```

Or with input piped from another command:

```bash
cat file.json | jq '<filter>'
```

### Examples

1. **Pretty-Print JSON**

```bash
jq '.' data.json
```

Outputs formatted nicely indented JSON.

2. **Extract Keys or Values**

Extract the value of key `name`:

```bash
jq '.name' data.json
```

3. **Filter Arrays**

Select array elements where `age` > 30:

```bash
jq '.[] | select(.age > 30)' data.json
```

4. **Map and Transform**

Add a new field `isAdult` based on `age`:

```bash
jq '.[] | .isAdult = (.age >= 18)' data.json
```

5. **Combine and Compose Filters**

Get the names of adults older than 18:

```bash
jq '.[] | select(.age >= 18) | .name' data.json
```

6. **Using Variables**

Assign and reuse variables within filters:

```bash
jq --arg city "London" '.[] | select(.city == $city)' data.json
```

### Best Practices

- Quote filters properly to avoid shell interpolation issues.
- Use streaming options (`--stream`) on large files.
- Combine filters to create composable and readable queries.
- Use modules and custom functions for reusable queries.

---

## API Reference

While `jq` is a command-line tool, it provides a rich built-in expression language and functions. Additionally, it offers a C API for embedding `jq` functionality into other programs.

### Command-Line Options (Execution Facts)

- `-c`: Compact output (no pretty printing).
- `-r`: Raw output (output strings without JSON quotes).
- `-s`: Slurp. Read all inputs into a single array.
- `-n`: Don't read any input; start with `null`.
- `--stream`: Parse input in streaming fashion (produces arrays of path and leaf values).
- `--arg name value`: Set a variable accessible in the filter.
- `--argjson name value`: Set a variable from a JSON value.

### Core Filter Syntax and Functions

- `.foo` - Select field `foo`.
- `.[]` - Iterate over array elements.
- `select(condition)` - Filters inputs by condition.
- `map(expression)` - Transforms arrays.
- `length` - Returns length of array/object/string.
- Arithmetic: `+`, `-`, `*`, `/`, `%`.
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`.
- Logical: `and`, `or`, `not`.
- String functions: `startswith`, `endswith`, `contains`.
- Arrays and objects construction: `[ ... ]`, `{ key: value }`.
- Recursive descent: `..`.
- Functions: `keys`, `has`, `type`, `tonumber`, `tostring`, `explode`, `implode`.

### C API (General Facts)

- Embeds the `jq` engine to run filters from within C programs.
- Use `jq_init`, `jq_compile`, `jq_start`, and `jq_next` to process JSON values.
- Parse JSON inputs to `jv` values with `jv_parse`.
- Retrieve results as `jv` types for further manipulation.

---

## License

`jq` is open source software licensed under the MIT License. For full license details, see the [LICENSE](https://github.com/stedolan/jq/blob/master/LICENSE) file in the repository.
