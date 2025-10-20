```md
# jq Documentation

jq is a lightweight and flexible command-line JSON processor. It is designed to slice, filter, map, and transform structured JSON data effortlessly, making complex JSON manipulation accessible in shell scripts and other environments.

---

## Conceptual Introduction

### Domain Concepts

- **JSON (JavaScript Object Notation):** A lightweight data-interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
- **Filtering and Transformation:** jq allows applying programs (filters) to JSON inputs and outputs the transformed JSON or related data.
- **Filters:** Core jq constructs to extract and manipulate JSON data; can be elementary (like `.foo`) or combined (expressions, pipes).
- **Streams:** jq supports streaming JSON processing, enabling handling of large data inputs efficiently.
- **Modules:** jq supports modular filters letting users define reusable components.
- **Pipelines:** jq programs can be chained using pipes to combine multiple transformations.
- **Command Line Interface:** jq is most commonly used via CLI where JSON data is passed through jq with filter expressions.

### Mapping to API Terms

- The command line usage `jq [options] <filter> [file ...]` corresponds to applying jq filter programs to JSON inputs.
- The jq library exposes functions and data types like `jq_state` (interpreter state), `jv` (JSON value), and APIs to compile filters, execute them, and manipulate JSON data programmatically.
- Filters are parsed and compiled with APIs like `jq_compile` and executed via `jq_start` and `jq_next`.
- Options control behaviors such as raw output, sorting, debugging, slurping multiple JSON inputs.
- The library can be integrated into custom C programs to embed jq’s JSON processing engine.

---

## Execution Facts

### jq Command Line Execution

| Feature/Option                 | Input                                           | Output                                 | Errors / Side Effects                                | Defaults / Constraints                         |
|-------------------------------|------------------------------------------------|---------------------------------------|-----------------------------------------------------|------------------------------------------------|
| `jq <filter> [file ...]`        | JSON input via file or stdin; jq filter string | Filtered JSON or text output           | Errors if input not valid JSON or filter malformed  | Reads STDIN if no file; UTF-8 expected         |
| `-r, --raw-output`             | Output raw strings instead of JSON quotes       | Raw strings or text output             | N/A                                                 | Default is JSON output                          |
| `-c, --compact-output`         | Compact JSON output on one line                  | JSON output in compact form            | N/A                                                 | Default outputs pretty-printed JSON            |
| `-s, --slurp`                 | Read entire input stream into an array           | Array containing JSON objects          | N/A                                                 | Default processes inputs one at a time          |
| `-f, --from-file`              | Read filter program from file                     | Applies filter loaded from file        | Errors on file missing or invalid filter            | Filter can also be provided as argument        |
| `--stream`                    | Parse JSON inputs as stream tokens                | Stream JSON token objects               | Enables processing large inputs                      | Streaming disables some features                |

### jq C Library APIs (Selected)

| Function                     | Inputs                                                   | Outputs                                   | Errors / Side Effects                              | Notes/Usage                                                        |
|------------------------------|----------------------------------------------------------|-------------------------------------------|----------------------------------------------------|------------------------------------------------------------------|
| `jq_init()`                  | None                                                     | Returns new jq interpreter state (`jq_state*`) | Allocates interpreter state                         | Must call `jq_teardown` to free                                  |
| `jq_compile(jq_state*, jv filter)` | jq interpreter, filter as JSON value                      | Compilation status as boolean              | NULL if compilation fails                            | Compiles filter for later execution                              |
| `jq_start(jq_state*, jv input, int flags)` | Begin filter evaluation with given input                  | Boolean status                             | Input JSON ownership transferred                   | Flags control evaluation options                                 |
| `jq_next(jq_state*)`         | Interpreter state                                        | Next output value `jv` or NULL if done     | Outputs must be freed by caller                      | Called repeatedly to fetch all filter outputs                    |
| `jv_parse(const char*)`      | String containing JSON text                             | Parsed `jv` value or error                  | NULL on parse failure                                | Parse JSON strings for inputs                                    |
| `jv_dump(jv, int flags)`     | JSON value and flags (pretty, compact, raw)             | Prints JSON to stdout                       | Side effect: output to stdout                        | Used for output rendering                                        |
| `jq_teardown(jq_state*)`     | Interpreter state                                        | Frees resources                            | Cleans interpreter state                             | Must be called to avoid leaks                                   |

---

## API Usage Patterns

### Pattern 1: Using jq CLI for JSON Transformation

#### What the code does

- Applies jq filter expressions to modify or extract JSON data piped via input files or stdin.
- Outputs transformed JSON or raw text to stdout or files.

#### How it does it

- Command line accepts filter expressions and options.
- Parses JSON inputs.
- Applies filters to inputs producing JSON output or text.
- Supports slurping multiple JSON objects into arrays.
- Options control output formatting.

#### Why it’s structured that way

- CLI tool is versatile to fit multiple usage scenarios: quick one-liners or complex scripts.
- Options provide control over output format for easy shell pipeline integration.
- Streaming supports large data processing.

#### Variation Points

- Filters can be simple field selectors like `.foo` or complex constructs involving map, reduce, conditionals.
- Use `-r` for extracting raw strings from JSON.
- Employ `--stream` for large JSON processing.
- Chain filters using pipes (`|`) for multi-step transformations.

---

### Pattern 2: Embedding jq in C Programs

#### What the code does

- Creates an embedded jq interpreter to process JSON within a C application.
- Compiles and runs jq filters programmatically.
- Iterates over outputs to handle JSON results.

#### How it does it

- Initialize jq interpreter state `jq_init()`.
- Parse filter string JSON representation to `jv`.
- Compile filter with `jq_compile`.
- Parse input JSON strings to `jv`.
- Start evaluation with `jq_start`.
- Iteratively call `jq_next` to receive output JSONs.
- Clean up with `jq_teardown`.

#### Why it’s structured that way

- Provides a programmatic, reusable approach to JSON processing with jq’s powerful filtering engine.
- Decouples JSON parsing/transformation from command line, enabling high-performance embedded use.
- Lifecycle API manages resources correctly.

#### Variation Points

- Use JSON streaming APIs for large or partial JSON inputs.
- Combine with custom C code to integrate jq results into application logic.
- Adjust interpreter flags for different evaluation strategies.

---

## Example Pattern: CLI Usage to Filter JSON and Output Raw Text

```bash
echo '{"name":"Alice","age":30,"city":"New York"}' | jq -r '.name'
```

- **What:** Extracts the `name` field from JSON and outputs it as raw text without quotes.
- **How:** Runs jq with filter `.name` and raw output option `-r`; input piped via echo.
- **Why:** Demonstrates simple extraction of a value for use in scripts.
- **Variation:** Change filter to `.city` or other fields; omit `-r` to get JSON quoted output.

---

## Example Pattern: Embedding jq in C to Apply Filter

```c
#include <jq.h>
#include <jv.h>
#include <stdio.h>

int main(int argc, char *argv[]) {
    // Initialize jq state
    jq_state *jq = jq_init();

    // Compile filter
    jv filter = jv_parse(".foo");
    if (!jq_compile(jq, filter)) {
        fprintf(stderr, "Failed to compile filter\n");
        return 1;
    }

    // Parse input JSON
    jv input = jv_parse("{\"foo\": \"bar\"}");
    jq_start(jq, input, 0);

    // Iterate outputs
    jv result;
    while ((result = jq_next(jq)) != NULL && !jv_is_null(result)) {
        jv_dump(result, 0);
        jv_free(result);
    }

    // Teardown
    jq_teardown(&jq);
    return 0;
}
```

- **What:** Compiles and applies filter `.foo` to JSON with field `foo`, outputs the value.
- **How:** Uses jq C API to compile and execute filter, parse input, fetch results.
- **Why:** Illustrates embedding jq processing in native C code.
- **Variation:** Change filter JSON or input JSON; handle errors for production use.

---

## Additional Developer Notes

- jq filters follow a functional and compositional syntax that requires some learning but offers great power.
- The jq manual and online playgrounds are a resource to build filters incrementally.
- jq streams and slurp features address performance and memory when working with large JSON data.
- Embedding jq requires linking with jq library and managing memory for `jv` values carefully.
- Command line options enable interoperability and scripting convenience beyond simple filters.

---

This documentation integrates jq’s core domain concepts of JSON processing and filtering, explicit execution facts for its CLI and C API usage, and detailed usage patterns to empower developers for flexible JSON manipulation.
```
