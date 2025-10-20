```md
# jq Documentation

jq is a lightweight and flexible command-line JSON processor. It allows developers and users to parse, filter, transform, and manipulate JSON data with a powerful and expressive query language. jq is widely used for JSON data processing tasks in shell scripts, data pipelines, and other automation scenarios.

---

## Conceptual Introduction

### Domain Concepts

- **JSON (JavaScript Object Notation):** A lightweight data interchange format that is easy for humans to read and write and easy for machines to parse and generate.
- **jq Processor:** A command-line tool that reads JSON input and transforms it using jq’s query language.
- **Filters:** jq programs that specify how to transform or extract data from JSON documents.
- **Streaming:** jq can process large JSON inputs efficiently using streaming mode.
- **Modules:** jq supports loading and using external jq modules to extend functionality.
- **Pipelines:** jq filters can be chained together, making complex transformations modular and clear.

### Mapping to API Terms

- The core jq executable runs with a jq program (filter) and JSON input.
- Filters are expressed in jq’s own functional programming language designed for JSON.
- The library exposes functions and data structures to parse JSON, compile filters, and run them on data.
- jq can be embedded as a library in other applications, or used as a standalone CLI.

---

## Execution Facts

### Core Components and APIs

| API Element              | Inputs                                            | Outputs                  | Errors / Side Effects                              | Defaults / Constraints                      |
|--------------------------|--------------------------------------------------|--------------------------|---------------------------------------------------|---------------------------------------------|
| `jq_compile(filter_str)`  | `filter_str: string` - jq filter expression      | Compiled jq filter object | Returns errors if filter syntax is invalid        | Filter string must be valid jq syntax       |
| `jq_run(filter, json_input)` | `filter`: compiled filter object, `json_input`: JSON data (string or parse tree) | Filter output as JSON(s) | May error on invalid input or runtime exceptions  | Memory and processing limits apply           |
| jq CLI invocation        | Command line with filter and JSON input           | Transformed JSON output   | Possible parse or runtime errors output as messages| Input can be from file, stdin, or inline JSON |

### CLI Execution Facts

| Command                      | Description                                   | Inputs                      | Outputs              | Constraints & Notes                           |
|------------------------------|-----------------------------------------------|-----------------------------|----------------------|-----------------------------------------------|
| `jq <filter> <file>`          | Runs filter on a JSON file                     | jq program (filter), JSON file or stdin | Filtered JSON output | Supports range of filters, files, stdin      |
| `jq --slurp`                  | Slurps multiple JSON inputs into an array     | JSON array input             | JSON output of array  | Useful for batch processing                  |
| `jq --stream`                 | Enables streaming parser mode                   | Large JSON input             | Streamed filtered output | Optimizes for memory efficiency               |
| `jq -c`                      | Compact output, JSON objects printed without pretty formatting | JSON input, filter            | Compact JSON output   | Useful for scripting                           |
| `jq -r`                      | Output raw strings, no quotes                      | JSON input, filter            | Raw text output       | For command substitution or text output       |

### Library Embedding Facts

- jq can be embedded using its API in C programs.
- Provides interfaces to parse JSON, compile filters, and iterate over results.
- Supports control over memory allocation and error reporting.

---

## API Usage Patterns

### Pattern 1: Command-Line JSON Processing

#### What the code does

Runs jq filters on JSON files or standard input to extract or transform JSON data for use in shell pipelines or scripting.

#### How it does it

- Accepts a jq filter expression.
- Parses and validates the filter.
- Reads JSON input from files or standard input.
- Executes filter on the input producing JSON output.
- Supports output formatting options (compact, raw, streaming).

#### Why it’s structured that way

- Provides an easy-to-use tool for quick JSON manipulation.
- Supports complex JSON transformations using a concise, expressive language.
- Fits naturally into Unix-style data processing pipelines.

#### Variation Points

- Use different filters for extraction, transformation, aggregation.
- Enable `--slurp` to combine multiple JSON objects into an array.
- Use `--stream` mode for processing very large JSON inputs efficiently.
- Control output formatting using flags `-c` and `-r`.

---

### Pattern 2: Embedding jq in Applications

#### What the code does

Uses the jq library APIs to compile filter expressions, pass JSON data, execute filtering, and retrieve JSON results programmatically inside another application (usually C/C++).

#### How it does it

- Calls `jq_compile` to create a filter object.
- Feeds JSON input to the filter.
- Invokes jq runtime to execute filter logic.
- Iterates over or collects output JSONs.
- Handles errors and memory management explicitly.

#### Why it’s structured that way

- Enables integration of jq’s powerful JSON querying language into custom software.
- Allows for high performance and greater control over JSON processing.
- Provides error handling and detailed control for robust embedding.

#### Variation Points

- Manage jq state lifecycle carefully for multiple runs.
- Combine multiple jq filters programmatically.
- Integrate jq outputs into broader application logic.

---

## Example Pattern: CLI JSON Filtering and Output

```bash
# Extract all names from an array of user objects
jq '.users[].name' users.json

# Output each name as a raw string, one per line
jq -r '.users[].name' users.json

# Combine multiple JSON files into a single array and extract all ids
jq --slurp '[.[][]] | map(.id)' file1.json file2.json

# Stream processing - count number of objects in a large array
jq --stream 'select(.[0]|length == 0) | length' large.json
```

- **What:** These examples demonstrate filtering JSON data, extracting values, combining JSON inputs, and streaming large JSON efficiently.
- **How:** By using jq filters and CLI options to transform data as needed.
- **Why:** Showcases jq’s versatility in different scenarios from simple extraction to advanced use.
- **Variation:** Change filters to adapt to various JSON structures; adjust output modes for scripting.

---

## Example Pattern: Embedding jq in C Application

```c
#include <jq.h>
#include <stdio.h>

int main() {
    jq_state *jq = jq_init();
    if (!jq) {
        fprintf(stderr, "Failed to initialize jq\n");
        return 1;
    }

    // Compile the filter
    if (!jq_compile(jq, ".foo")) {
        fprintf(stderr, "Failed to compile filter\n");
        jq_teardown(&jq);
        return 1;
    }

    // Set the input JSON string
    const char *json = "{\"foo\": 42, \"bar\": 100}";
    jv input = jv_parse(json);

    jq_start(jq, input, 0);

    jv result;
    while (jv_is_valid(result = jq_next(jq))) {
        if (!jv_is_null(result)) {
            char *s = jv_dump_string(result, 0);
            printf("Result: %s\n", s);
            free(s);
        }
        jv_free(result);
    }

    jv_free(input);
    jq_teardown(&jq);
    return 0;
}
```

- **What:** This example shows embedding jq in a C program to extract the `.foo` field from JSON.
- **How:** Initializes jq, compiles a filter, runs it on input JSON, and prints results.
- **Why:** Demonstrates jq’s embedding API for programmatic JSON processing.
- **Variation:** Change filter string or input JSON as needed; add error handling for robustness.

---

## Additional Developer Notes

- jq supports a rich query language with many built-in functions and filters: see the jq manual for full details.
- jq syntax errors and runtime errors are output with explanations in CLI mode.
- Streaming mode is recommended for very large JSON inputs to reduce memory footprint.
- Embedding jq requires managing jq state and JV values carefully to avoid leaks.
- jq can read filters from files or as inline strings.
- Extensive documentation and community examples are available at https://stedolan.github.io/jq/ and GitHub repository.

---

This documentation integrates the domain concepts of JSON processing and jq filtering, execution facts about jq CLI and library APIs, and usage patterns to provide a robust foundation for users and developers leveraging jq for JSON data transformation tasks.
```

