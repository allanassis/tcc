```md
# jq Lang Documentation

jq is a powerful, lightweight, and flexible command-line JSON processor. It allows users to slice, filter, map, and transform structured JSON data with a high-level functional programming style. Originally written in C, jq provides a compact domain-specific language to query and manipulate JSON inputs programmatically or interactively.

---

## Conceptual Introduction

### Domain Concepts

- **JSON (JavaScript Object Notation):** A lightweight data interchange format that's easy for humans to read/write and machines to parse/generate.
- **jq Filter:** A piece of code or expression written in jq's domain-specific language that processes JSON data, transforming it or extracting information.
- **Stream Processing:** jq processes JSON input streams element by element allowing it to handle large or continuous JSON data efficiently.
- **Pipelines:** jq filters can be chained or combined, enabling modular transformations.
- **Objects and Arrays:** jq natively understands the JSON data model including objects, arrays, strings, numbers, booleans, and null.
- **Functions and Variables:** jq supports defining reusable functions and variables within filters for clarity and reusability.
- **Command-line Usage:** jq is primarily a command-line tool that reads JSON from stdin or files and outputs the transformed JSON on stdout.

### Mapping to API Terms

- The primary user interface is the jq executable, where filters are passed as arguments.
- The core API revolves around composing jq filters to extract or output JSON.
- Library embeddings (C API) allow integration of jq functionalities into other programs.
- Filters include built-in functions and operators to navigate and modify JSON structures.
- jq supports modular scripts via includes and programmatic invocation.
- Filters are typically small programs or expressions that transform input JSON into desired output.

---

## Execution Facts

### Command-Line Interface (CLI) Facts

| Command                          | Inputs                                | Outputs                          | Errors / Side Effects                         | Defaults / Constraints                       |
|---------------------------------|-------------------------------------|---------------------------------|-----------------------------------------------|----------------------------------------------|
| `jq [options] <filter> [file...]` | `filter`: jq expression string, `file(s)`: JSON input or stdin if omitted | Transformed JSON printed to stdout | Syntax errors in filter; ill-formed JSON input; file errors | Default output pretty-printed JSON; exit status for errors |

- Important options:
  - `-c` : Output JSON compactly (no pretty-print).
  - `-r` : Output raw strings, not JSON-encoded.
  - `--stream` : Parses input as a stream of JSON fragments.
  - `--slurp` (`-s`): Reads entire input into an array.
  - `--arg name value`: Pass external arguments into the filter.
  - `-f file` : Read filter program from file.
  - `-n` : Don't read input, operate on null.

### Library API (C API)

- Initialization and cleanup functions: `jq_init()`, `jq_teardown()`.
- Compile a filter string into executable form.
- Feed JSON input to the jq interpreter.
- Obtain JSON output programmatically.
- Manage callbacks and error handling.

### Filter Execution Facts

- Filters operate on JSON values.
- Outputs zero or more JSON results per input.
- Errors propagate and cause jq to report failure.
- Filters can recurse, iterate arrays or objects, and perform arithmetic or logical operations.
- Variables can be dynamically bound.
- Functions can be defined and invoked with arguments.

### Constraints and Environment

- jq is implemented in portable C supporting multiple OS platforms (Unix, Windows).
- Requires standard JSON formatted input.
- Large JSON input may be handled with streaming or slurping modes.
- Command-line environment expected for operation, though embeddable in other programs.
- Strict syntax enforcement in filters and JSON inputs.

---

## API Usage Patterns

### Pattern 1: Basic JSON Filtering and Extraction

#### What the code does

Filters JSON input to extract or transform parts. For example, extracting all values of a key or selecting array elements.

#### How it does it

- A jq filter expression is passed on the command line or script.
- JSON input is parsed and supplied to the filter.
- Filter expressions use built-in operators like `.foo` to access keys, `[index]` for arrays.
- Output is printed to stdout.

#### Why it’s structured that way

- Provides simple declarative syntax to access nested JSON.
- Enables easy command-line processing without writing full programs.
- Supports composability of operations for complex queries.

#### Variation Points

- Use `-r` to output raw strings (e.g. extracting URL strings for shell piping).
- Combine filters with pipes `|` for multi-step transformations.
- Use `--slurp` to read multi-document input as an array.

---

### Pattern 2: JSON Transformation and Mapping

#### What the code does

Transforms JSON structures by mapping input arrays or objects into new forms, adding or modifying keys or values.

#### How it does it

- Uses constructs like `map()`, `with_entries()`, or recursive filters.
- Supports defining functions for reusable transformations.
- Combines filters with conditional logic such as `if-then-else`, and arithmetic operators.

#### Why it’s structured that way

- Enables complex data reshaping in simple filter expressions.
- Leverages jq’s functional programming model for clear transformations.
- Facilitates pipelines transforming JSON stepwise.

#### Variation Points

- Create custom functions for reusable logic.
- Use `--argjson` and variables for external input parameters.
- Chain multiple filters in a script file with `-f`.

---

### Pattern 3: Streaming Parsing and Large Data Processing

#### What the code does

Processes very large JSON inputs or streams without loading entire documents into memory.

#### How it does it

- Uses the `--stream` option to parse input iteratively as (path, value) pairs.
- Construct filters that process or transform streamed fragments.
- Outputs JSON snippets progressively.

#### Why it’s structured that way

- Reduces memory footprint for large JSON files.
- Enables real-time processing of JSON data.
- Provides fine-grained control over input processing.

#### Variation Points

- Combine with `select()` filters to extract particular paths.
- Use `fromstream` and `tostream` helpers for converting between streaming and normal JSON.

---

## Example Patterns

### Example 1: Extract all "name" values from a JSON array

```bash
jq '.[] .name' input.json
```

- **What:** Outputs the "name" field of each element in the root JSON array.
- **How:** The filter `.[] .name` iterates over array elements and accesses their "name" key.
- **Why:** Demonstrates basic extraction and navigation.
- **Variation:** Add `-r` to output plain strings without quotes.

---

### Example 2: Transform an array of objects to only include selected keys

```bash
jq 'map({id, name})' input.json
```

- **What:** Converts each object in the root array to a new object only with keys `id` and `name`.
- **How:** Uses `map()` to apply the filter to each array element, creating new objects.
- **Why:** Shows JSON shaping with mapping.
- **Variation:** Add computed fields or filter objects conditionally.

---

### Example 3: Streaming parse and extract all string values

```bash
jq --stream 'select(length == 2 and .[1] | type == "string") | .[1]'
```

- **What:** From streamed input, filters all string values and outputs just the strings.
- **How:** Uses streaming mode to process JSON as chunks, filters by path-value pair length and type.
- **Why:** Demonstrates streaming filtering for large JSON.
- **Variation:** Adjust selector to extract other data types or paths.

---

## Additional Developer Notes

- jq’s language is Turing complete and supports advanced functional programming constructs including conditionals, recursion, and first-class functions.
- Comprehensive manual available online with detailed descriptions of built-in functions and examples.
- Error messages specify problems with JSON input or filter syntax.
- jq is highly optimized, suitable for scripting, automation, and embedding.
- Embedding the jq library allows integration of JSON processing capabilities into C programs.
- Community-driven with multiple third-party jq modules and tooling.

---

This documentation integrates jq’s domain concepts of JSON processing, execution facts about command line options and filter semantics, and usage patterns illustrating practical JSON querying and transformation workflows to provide a robust understanding for users and developers.
```
